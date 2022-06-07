from django.urls import URLPattern, path

from . import views

app_name = 'draft'
urlpatterns = [
    path('', views.index, name='home'),
    path('select/<int:id>/', views.select, name='select'),
]
