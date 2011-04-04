from django.core.management.base import BaseCommand, CommandError

from callingtool.models import LegislatorDetail
from uspolitics.politicians.models import Politician

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        
        LegislatorDetail.objects.all().delete()
        
        for pol in Politician.objects.filter(in_office=True):
            LegislatorDetail.objects.create(
                legislator=pol,
                on_bill='U',
                on_amendment=None,
                call_goal=10,
            )