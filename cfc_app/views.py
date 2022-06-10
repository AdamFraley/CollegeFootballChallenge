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


    context = {
        'teams' : teams,
        'conferences' : conferences,
        'divisions' : divisions,
        'message' : message,
        'players' : players,
        'draft' : draft,
    }

    print(request.GET.get('message'))

    return render(request, 'cfc_app/index.html', context)

def select(request,id):
    selected_team = FbsTeam.objects.get(id=id)
    draft = Draft.objects.first()
    pick = Pick.objects.get(pick_number=draft.current_pick)

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
    draft.create_draft_order()
    return redirect('draft:home')

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