from django.db import models

class MissionVisionObjective(models.Model):
    mission = models.TextField()
    vision = models.TextField()
    objectives = models.TextField()

class Startup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    founder = models.CharField(max_length=255)
    founded_date = models.DateField()

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()

class GoverningBodyMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.EmailField()
