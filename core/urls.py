from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('ps3/', views.ps3_collection, name='ps3_collection'),
    path('ps3/standard/', views.standard_games, name='standard_games'),
]
