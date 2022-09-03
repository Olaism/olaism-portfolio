from django.contrib import admin

from .models import Profile, About, Skill, Project

admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Project)
