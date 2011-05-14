from django.db import models
from tagging.fields import TagField

class Institution(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    tags = TagField()

    def __unicode__(self):
        return self.title
