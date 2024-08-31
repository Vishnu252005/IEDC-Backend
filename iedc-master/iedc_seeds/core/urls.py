from django.urls import path
from . import views

urlpatterns = [
    path('home-page/', views.home_page,name='home-page'),
    path('registration/', views.registration_view, name='registration'),
]
