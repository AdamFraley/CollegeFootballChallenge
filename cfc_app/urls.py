from django.urls import URLPattern, path

from . import views

app_name = 'draft'
urlpatterns = [
    path('', views.index, name='home'),
    path('select/<int:id>/', views.select, name='select'),
    path('create-draft/', views.create_draft),
    path('reset-teams-picks/', views.reset_teams_picks),
    path('reset-draft-order/', views.reset_draft_order),
]
