from django.db import models

class Password(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=14)
