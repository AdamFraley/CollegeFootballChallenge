from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Conference, Division, FbsTeam, Draft, Pick
from players.models import User
from django.contrib.auth.decorators import user_passes_test


def index(request):
    teams = FbsTeam.objects.all()
    conferences = Conference.objects.all()
    divisions = Division.objects.all()
    message = request.GET.get('message')
    draft = Draft.objects.first()
    players = draft.players.order_by('draft_order')
    current_pick = draft.current_pick
    pick = None
    if current_pick < 57 and draft.live:
        pick = Pick.objects.get(pick_number=draft.current_pick)
        users_turn = pick.player == request.user
    else:
        users_turn = False

    context = {
        'teams' : teams,
        'conferences' : conferences,
        'divisions' : divisions,
        'message' : message,
        'players' : players,
        'draft' : draft,
        'users_turn' : users_turn,
        'current_pick' : current_pick,
        'pick' : pick,
    }

    print(request.GET.get('message'))

    return render(request, 'cfc_app/index.html', context)

def select(request,id):
    selected_team = FbsTeam.objects.get(id=id)
    draft = Draft.objects.first()
    pick = Pick.objects.get(pick_number=draft.current_pick)
    teams_owned = FbsTeam.objects.filter(owned__isnull=False).count()

    if teams_owned == 56:
        return redirect('draft:home')
    else:
        if not request.user.is_superuser:
            if pick.player != request.user:
                return redirect('/?message=Its+not+your+turn')

            selected_team.owned = request.user
            selected_team.save()
            pick.team = selected_team
            pick.save()
            draft.current_pick += 1
            draft.save()
            print(selected_team)
            return redirect('draft:home')
        else:
            return redirect('/?message=admin+cannot+select+teams')

@user_passes_test(lambda u: u.is_superuser)
def create_draft(request):
    draft = Draft.objects.first()
    players = list(draft.players.all())
    if len(players) == 7:
        draft.live = True
        draft.save()
        draft.create_draft_order()
        return redirect('draft:home')
    else:
        return redirect('/?message=DRAFT+MUST+HAVE+7+PLAYERS')


@user_passes_test(lambda u: u.is_superuser, '/?message=resetting teams denied')
def reset_teams_picks(request):
    FbsTeam.objects.update(owned=None)
    Pick.objects.update(team=None)
    return HttpResponse('reset all teams to not owned - reset all picks to None')

@user_passes_test(lambda u: u.is_superuser, '/?message=YOU+cant+reset+the+draft+order')
def reset_draft_order(request):
    User.objects.update(draft_order=None)
    Draft.objects.update(current_pick=1)
    Pick.objects.all().delete()
    return redirect('draft:home')

@user_passes_test(lambda u: u.is_superuser, '/?message=YOU+cant+reset+the+draft+order')
def reset_draft(request):
    FbsTeam.objects.update(owned=None)
    Pick.objects.update(team=None)
    User.objects.update(draft_order=None)
    Draft.objects.update(current_pick=1, live=False)
    Pick.objects.all().delete()
    return redirect('draft:home')

@user_passes_test(lambda u: u.is_superuser, '/?message=YOU+cant+reset+the+draft+order')
def undo_last_pick(request):
    draft = Draft.objects.first()
    draft.current_pick -= 1
    draft.save()
    pick = Pick.objects.get(pick_number=draft.current_pick)
    team = pick.team
    team.owned = None
    team.save()
    pick.team = None
    pick.save()
    return redirect('draft:home')

def rules(request):
    return render (request, 'cfc_app/rules.html')

@user_passes_test(lambda u: u.is_superuser, '/?message=YOU+cant+reset+the+draft+order')
def draft_end_test(request):
    teams_owned = FbsTeam.objects.filter(owned__isnull=False).count()
    print(teams_owned)
    return HttpResponse('testing number of owned teams')

def roster(request):
    teams = FbsTeam.objects.all()
    draft = Draft.objects.first()
    players = draft.players.order_by('draft_order')



    context = {
        teams : 'teams',
        players : 'players',
    }

    return render (request, 'cfc_app/roster.html')
