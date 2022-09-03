from markdown import markdown

from django.utils.html import mark_safe
from django.db import models
from django.urls import reverse

class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    job = models.CharField(max_length=30)
    describe_yourself = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class About(models.Model):
    heading = models.CharField(max_length=125)
    details = models.CharField(max_length=255)

    def __str__(self):
        return self.heading[:10]

class Skill(models.Model):
    class_name = models.CharField(max_length=25, blank=True, default="")
    name = models.CharField(max_length=30)
    skill_range = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Project(models.Model):
    cover_image = models.URLField(max_length=125, null=True, blank=True)
    title = models.CharField(max_length=145)
    demo = models.URLField(blank=True, null=True)
    code = models.URLField(blank=True, null=True)
    highlight = models.CharField(max_length=255, default="", blank=True)
    details = models.TextField(blank=True, null=True)
    program = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})

    def get_details_as_markdown(self):
        return mark_safe(markdown(self.details, safe_mode='escape'))