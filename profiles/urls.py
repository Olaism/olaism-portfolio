from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/get-in-touch', views.contact, name='contact'),
    path('/about', views.about, name='about'),
    path('/skills', views.skills, name='skills'),
    path('/projects', views.projects, name='projects'),
]