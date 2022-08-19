from django.core.management.base import BaseCommand
from cfc_app.models import Division, Conference

import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('divisions')

        with open('csv/cfc_division.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # print(row)
                conference = Conference.objects.get(name=row['conference_name'])
                Division.objects.get_or_create(
                    name = row['name'],
                    conference = conference,
                )




