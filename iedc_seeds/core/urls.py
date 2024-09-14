from django.urls import path
from core.views import HomePageView, RegistrationView, RegisteredUsersView

urlpatterns = [
    path('', HomePageView.as_view() ,name='home-page'),
    path('registration/', RegistrationView.as_view() , name='registration'),
    path('registered-users/', RegisteredUsersView.as_view() , name='registered_users'),
]
