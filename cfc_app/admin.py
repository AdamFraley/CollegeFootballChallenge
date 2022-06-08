from django.contrib import admin

from .models import FbsTeam, Conference, Division, League

admin.site.register(FbsTeam)
admin.site.register(Conference)
admin.site.register(Division)
admin.site.register(League)

