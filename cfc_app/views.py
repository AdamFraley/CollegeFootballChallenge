import re
from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Conference, Division, FbsTeam

def index(request):
    teams = FbsTeam.objects.all()
    conferences = Conference.objects.all()
    divisions = Division.objects.all()
    message = request.GET.get('message')

    context = {
        'teams' : teams,
        'conferences' : conferences,
        'divisions' : divisions,
        'message' : message,
    }

    print(request.GET.get('message'))

    return render(request, 'cfc_app/index.html', context)

def select(request,id):
    selected_team = FbsTeam.objects.get(id=id)
    if not request.user.is_superuser:
        selected_team.owned = request.user
        selected_team.save()
        return redirect('draft:home')
    else:
        return redirect('/?message=admin+cannot+select+teams')

