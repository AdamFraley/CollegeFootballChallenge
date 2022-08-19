from django.core.management.base import BaseCommand
from cfc_app.models import Conference

import csv

# print(hello)

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('conferences')

        with open('csv/cfc_conference.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Conference.objects.get_or_create(
                    name = row['name'],
                    abbreviation = row['abbreviation'],
                )




