from django.shortcuts import render

from .models import (
    Profile,
    About,
    Skill,
    Project
)

def home(request):
    return render(request, 'profiles/home.html')

def contact(request):
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