from django.urls import URLPattern, path

from . import views

app_name = 'draft'
urlpatterns = [
    path('', views.index, name='home'),
    path('select/<int:id>/', views.select, name='select'),
    path('create-draft/', views.create_draft),
    path('reset-teams-picks/', views.reset_teams_picks),
    path('reset-draft-order/', views.reset_draft_order),
    path('reset-draft/', views.reset_draft),
    path('undo-last-pick/', views.undo_last_pick),
    path('rules/', views.rules, name='rules'),
    path('draft-end-test/', views.draft_end_test),
    path('roster/', views.roster, name='roster'),
]
