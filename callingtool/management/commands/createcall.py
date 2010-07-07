from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from optparse import make_option

from callingtool.models import LegislatorDetail
from simplesurvey.models import Question, QuestionSet
from uspolitics.politicians.models import Politician

QUESTIONS = (
    {'type': 'M', 'answer_choices': 'yes|no|unsure', 'text': 'on_bill'},
    {'type': 'S', 'answer_choices': '', 'text': 'name'},
    {'type': 'S', 'answer_choices': '', 'text': 'email'},
    {'type': 'S', 'answer_choices': '', 'text': 'zip'},
    {'type': 'L', 'answer_choices': '', 'text': 'comments'},
)

class Command(BaseCommand):
    
    option_list = BaseCommand.option_list + (
        make_option('-t', '--title', dest='title', metavar='"CALL TITLE"', help='name of campaign'),
        make_option('-d', '--description', dest='desc', metavar='"CALL DESCRIPTION"', help='description of campaign'),
    )
    
    def handle(self, *args, **options):
        
        if not options['title'] or not options['desc']:
            raise CommandError('title and description arguments are required')
        
        qs = QuestionSet(
            slug=slugify(options['title']),
            title=options['title'],
            description=options['desc'],
            allow_anonymous=True,
            allow_multiple_responses=True,
            enabled=True,
        )
        qs.save()
        
        order = 1
        for q in QUESTIONS:
            Question(question_set=qs, order=order, required=True, **q).save()
            order += 1
