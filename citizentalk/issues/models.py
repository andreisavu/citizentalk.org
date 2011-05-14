from django.db import models
import tagging

class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField('date created', auto_now_add = True)
    updated_at = models.DateTimeField('date updated', auto_now = True)

tagging.register(Issue)
