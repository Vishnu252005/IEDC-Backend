from django.shortcuts import render, redirect 
from .models import Registrant
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegistrationForm  

def home_page(request):
     return render(request,'index.html')

def registration_page(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        event = request.POST.get("postSno")
        date = Post.objects.get("date")

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Registration successful!')
            return redirect('registration') 
    else:
        form = RegistrationForm() 

    context = {
        'form': form,
    }
    return render(request, 'registration.html', context)


