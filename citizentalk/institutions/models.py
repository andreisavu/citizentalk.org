from django.db import models

class Institution(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
