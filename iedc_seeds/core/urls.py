from django.urls import path
from . import views

urlpatterns = [
    path('api/mission-vision-objectives/', views.mission_vision_objectives_view),
    path('api/startups/', views.startups_view),
    path('api/events/', views.events_view),
    path('api/governing-body-members/', views.governing_body_members_view),
]
