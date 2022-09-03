import os

from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail

from .models import (
    Profile,
    About,
    Skill,
    Project
)
from .forms import ContactForm

def home(request):
    profile = Profile.objects.first()
    return render(request, 'profiles/home.html', {'profile': profile})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            recipients = [os.environ.get('EMAIL_HOST_USER')]
            if subject and message and email:
                try:
                    send_mail(subject, message, email, recipients, fail_silently=True)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

                return redirect('/contact/thanks/')
            else:
                return HttpResponse('Make sure all fields are entered and valid.')

    else:
        form = ContactForm()
    return render(request, 'profiles/contact.html', {'form': form})

def about(request):
    about = About.objects.first()
    return render(request, 'profiles/about.html', {'about': about})

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'profiles/skills.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'profiles/projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'profiles/project_detail.html', {'project': project})