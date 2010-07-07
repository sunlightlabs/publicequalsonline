from django.core.management.base import BaseCommand, CommandError

from callingtool.models import LegislatorDetail

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        LegislatorDetail.objects.all().update(
            on_bill='U',
            on_amendment=None,
            call_goal=10,
        )