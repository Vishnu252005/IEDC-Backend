from django.db import models

class Registrant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    college = models.CharField(max_length=100)
    event = models.CharField(max_length=100)

    def __str__(self):
        return self.name
