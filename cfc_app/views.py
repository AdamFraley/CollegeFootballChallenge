from django.shortcuts import render

from django.http import HttpResponse

from .models import Conference, Division, FbsTeam

def index(request):
    teams = FbsTeam.objects.all()
    conferences = Conference.objects.all()
    divisions = Division.objects.all()

    context = {
        'teams' : teams,
        'conferences' : conferences,
        'divisions' : divisions,
    }

    return render(request, 'cfc_app/index.html', context)
