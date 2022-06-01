# Capstone College Football Challenge App

## Overview
For fantasy football players the College Football Challenge (CFC) is a game that allows players to form between a 6-8 person fantasy football league where players draft 8 FBS college football teams to form their CFC roster. Game play consists of 6 active spots and 2 bench spots each week through the regular season. Each player will choose 6 of their teams to put in an active spot. Each game will receive points based on the team's win either home or away, strenght of schedule bonus points, and upset points - all points only realized with a win. There is also a ranking bonus for the teams on a roster ranked in the AP poll at the end of each week - independent of win. [Other rules and points structure - post season(conference winners/bowl games), dropping/adding teams, trading teams]. 
### Goal
The goal of this project is to create a web app that will allow users to create a league and then conduct a draft of the 131 FBS teams from the 10 conferences and Independents. Maybe add the game play board feature with automated scoring through a few APIs. The project will be built in Django and Vue js.

## Features
#### I have played the College Football Challenge multiple years and we currently use a shared Google sheet to conduct the draft as well host the weekly game board. I would like to show each team that has been drated on the draft board as well as an updated list of FBS teams that have not been drafted.
* Create a django model of all FBS teams(team, image icon, conference affiliation, current AP ranking, owned by)
* Create a form for each user to fill out to register in the league with a username and password, establishing one player as the league commissioner.
* Create a view that shows all users in the leauge with their username and spots for their eight teams. Below this show a list of all the conferences with their respective teams and an indicator of whether they are owned yet or not (maybe their AP ranking as well).
* Create a view that shows and explains the scoring and other rules of play.

#### Once the league has been set we will need to randomly select the draft order of the users. Draft picks will continue in a 'snaking order' throughout the draft. 'Snaking Order' (for a 7 person league) would be the first player drafting 1st and then 14th, 15th, then 28th, 29th, etc, and the seventh player drafting the 7th, 8th and then 21st, 22nd, etc. until all players have drafted all 8 teams. This order will have the player with the 1st pick getting the last pick. There will also be a time limit (maybe set by the league if draft isn't live) 5 minutes to complete each draft pick for a live draft.
* Create code that will select a random order of players for the draft.
* With all players logged on, the commissioner would start the draft, which will create the draft order and put users on the draft board.
* Will allow the user to select a team from the list of teams. This will mark the team owned by that user and put them in their draft spot on the draft board. Once the player has selected their team the next player in the draft order will receive a notification that it is their turn to pick and their countdown clock would start. This will proceed until all players have picked all 8 of their teams.

## Schema (Data Model)
* Players
    - username (charfield)
    - draftorder (IntegerField)
* FBS Teams
    - School Name (charfield)
    - Conference Affiliation (charfield, conference/independent)
    - Owned (boolean field, foreign key to user, )
    - Ranking (integer field, AP ranking if any)
    - double down use (integer field, track teams that have been doubled)

## Schedule
### Week 1
* Create and clone Repo
* create virtual enviroment
* start Django project and connect the hoses
* write Django models

### Week 2
* populate database of FBS teams
* create view of player login/sign-up 
* create view of draft board
* add list of FBS teams to draft board view
* create alert pop-up for player draft turn
* create ability for player drafting to select a team from list

### Week 3
* create view of rules and scoring page

### Must Haves
* user creation
* draft board
* randomize draft order of players
* list of all FBS teams by conference
* show if teams are owned
* view of rules and scoring page

### Should Haves
* timer for draft moves
* ability to set timer
* Nice UI

### Can Haves
* Pre-season AP ranking of teams on list
* blog view for players to discuss trades and add/drops
* Regular season baord
    - API for weekly game match-ups
    - API for weekly AP ranking
* Post Season Board
    - API for post-season team bowls

