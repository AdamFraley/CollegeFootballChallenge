from django.core.management.base import BaseCommand
from cfc_app.models import FbsTeam, Conference, Division

import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('rankings')

        with open('csv/cfc_fbs_fpi.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # print(row)
                conference = Conference.objects.get(name=row['conference_name'])
                if conference.divisions.all().exists():
                    division = conference.divisions.get(name=row['division_name'])
                else:
                    division = None

                FbsTeam.objects.get_or_create(
                    school_name = row['school_name'],
                    nickname = row['nickname'],
                    conference_name = conference,
                    school_abbrev = row['school_abbrev'],
                    conference_abbrev = row['conference_abbrev'],
                    division_name = division,
                    fpi_ranking = row['fpi_rk'],
                    cbs_ranking = row['cbs_rank'],
                    ap_preseason_ranking = row['ap_ranking'],
                # if row['ap_ranking'] != 0:
                )
                    # FbsTeam.objects.get_or_create(
                    # )
