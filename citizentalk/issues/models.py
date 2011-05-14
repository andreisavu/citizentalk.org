from django.db import models
import tagging
from tagging.fields import TagField

class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField('date created', auto_now_add = True)
    updated_at = models.DateTimeField('date updated', auto_now = True)

tagging.register(Issue)

# horrible hack for failing tags overwrite
from tagging.models import Tag
Tag.name_any = property(lambda self: self.name)
