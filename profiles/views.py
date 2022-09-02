import os

from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .models import (
    Profile,
    About,
    Skill,
    Project
)
from .forms import ContactForm

def home(request):
    return render(request, 'profiles/home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            recipients = [os.environ.get('USER_EMAIL')]
            if subject and message and from_email:
                try:
                    send_mail(subject, message, email, recipients, fail_silently=True, 
                    auth_password=os.environ.get('USER_PASSWORD'))
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

                return redirect('/contact/thanks/')
            else:
                return HttpResponse('Make sure all fields are entered and valid.')

    else:
        form = ContactForm()
    return render(request, 'profiles/contact.html', {'contact': contact})

def about(request):
    about = About.objects.all()
    return render(request, 'profiles/about.html', {'about': about})

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'profiles/skills.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'profiles/projects.html', {'projects': projects})