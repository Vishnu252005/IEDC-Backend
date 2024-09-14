# from django.shortcuts import render, redirect 
from core.models import Registrant
from django.urls import reverse_lazy
from django.contrib import messages
from core.forms import RegistrationForm  
from django.views.generic import TemplateView, FormView, ListView

class HomePageView(TemplateView):
    template_name = 'index.html'

class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('registered_users')  

def form_valid(self, form):
        name = form.cleaned_data.get('name')
        event = form.cleaned_data.get('event') 

        try:
            registrant = Registrant.objects.get(event=event)
            date = registrant.date 
        except Registrant.DoesNotExist:
            form.add_error('event', 'Event not found')
            return self.form_invalid(form)

        form.save()

        messages.success(self.request, 'Registration successful!')
        return super().form_valid(form)

class RegisteredUsersView(ListView):
    model = Registrant
    template_name = 'registered_users.html'
    context_object_name = 'registrants' 

 


