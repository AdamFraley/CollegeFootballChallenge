from django.db import models
from players.models import User

class Conference(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=12, null=True)

    def __str__(self):
        return f'{self.abbreviation} - {self.name}'

class Division(models.Model):
    name = models.CharField(max_length=20)
    conference = models.ForeignKey(Conference, on_delete=models.PROTECT, related_name='divisions')

    def __str__(self):
        return f'{self.name} - {self.conference}'

class FbsTeam(models.Model):
    # list of teams for the challenge
    school_name = models.CharField(max_length=50)
    school_abbrev = models.CharField(max_length=10, null=True, blank=True)
    nickname = models.CharField(max_length=50)
    conference_name = models.ForeignKey(Conference, on_delete=models.PROTECT, null=True, related_name='teams')
    division_name = models.ForeignKey(Division, on_delete=models.PROTECT, null= True, blank=True, related_name='teams')
    conference_abbrev = models.CharField(max_length=12)
    owned = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    ranking = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.school_name} - {self.owned}' if self.owned != None else f'{self.school_name}'
        

