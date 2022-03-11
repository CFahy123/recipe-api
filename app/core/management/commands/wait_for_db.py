import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django Command to pause execution until db is available"""
    def handle(self, *args, **options):
        self.stdout.write('Waiting for databases...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailble, waiting 1 second...') 
                time.sleep(1) 
        self.stdout.write(self.style.SUCCESS('Database available!'))
