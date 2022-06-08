from django.contrib import admin

from .models import Draft, FbsTeam, Conference, Division, League, Pick

admin.site.register(FbsTeam)
admin.site.register(Conference)
admin.site.register(Division)
admin.site.register(League)
admin.site.register(Pick)
admin.site.register(Draft)

