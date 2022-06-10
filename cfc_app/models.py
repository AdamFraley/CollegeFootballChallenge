from re import T
from django.db import models
from players.models import User
import random

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
        
class League(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    player = models.ManyToManyField(User, blank=True)
    
    def __str__(self):
        return self.name

class Pick(models.Model):
    player = models.ForeignKey(User, on_delete=models.PROTECT, related_name='picks')
    pick_number = models.IntegerField(null=True, blank=True)
    team = models.OneToOneField(FbsTeam, on_delete=models.PROTECT, null=True, blank=True)
    draft = models.ForeignKey('Draft', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.player.username} - pick {self.pick_number} - {self.team}' if self.team != None else f'{self.player.username} - pick {self.pick_number}'

class Draft(models.Model):
    players = models.ManyToManyField(User)
    current_pick = models.IntegerField(default=1)

    def create_draft_order(self):
        from random import shuffle
        # print(self.players.all())
        players = list(self.players.all())
        # print(players)
        shuffle(players)
        # print(players)
        # print(players[0].username, players[0].draft_order)
        k = 1
        for player in players:
            player.draft_order = k
            player.save()
            print(player.username, player.draft_order)
            k += 1
        # give random numbers 1-7 for draft position to each player
        range_picks = (len(players) * 8) + 1
        # print(range_picks)
        player_draft_position = 1
        counting = 'up'
        for pick in range(1, range_picks):
            # print(f'{players[player_draft_position - 1]} has pick {pick}')
            Pick.objects.create(
                player = players[player_draft_position - 1],
                pick_number = pick,
                draft = self
            )
            player.save()
            if counting == 'up':
                if player_draft_position == 7:
                    counting = 'down'
                else:
                    player_draft_position += 1
            elif counting == 'down':
                if player_draft_position == 1:
                    counting = 'up'
                else:
                    player_draft_position -= 1
        return


