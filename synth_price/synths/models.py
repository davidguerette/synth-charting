from django.db import models

class Synth(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
