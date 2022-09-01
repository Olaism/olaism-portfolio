from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    describe_yourself = models.CharField(max_length=255)

class About(models.Model):
    heading = models.CharField(max_length=125)
    details = models.CharField(max_length=255)

class Skill(models.Model):
    icon = models.URLField(max_length=125)
    name = models.CharField(max_length=30)
    skill_range = models.PositiveIntegerField()

class Project(models.Model):
    cover_image = models.URLField(max_length=125, null=True, blank=True)
    title = models.CharField(max_length=145)
    demo = models.URLField(blank=True, null=True)
    code = models.URLField(blank=True, null=True)
    highlight = models.CharField(max_length=255, default="", blank=True)
    details = models.TextField(blank=True, null=True)
    program = models.CharField(max_length=255)