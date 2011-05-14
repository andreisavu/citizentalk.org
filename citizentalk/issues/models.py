from django.db import models
import tagging
from tagging.fields import TagField

class Attachment(models.Model):
    file = models.FileField(upload_to='file/%Y/%m/%d')
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

class Issue(models.Model):
    ISSUE_STATES = (
        (u'new', u'New'),
        (u'ass', u'Assigned'),
        (u'res', u'Resolved'),
        (u'acc', u'Accepted')
    )

    title = models.CharField(max_length = 200)
    description = models.TextField()

    state = models.CharField(max_length = 3, choices = ISSUE_STATES, default = 'new')

    latitude = models.DecimalField(max_digits = 15, decimal_places = 10)
    longitude = models.DecimalField(max_digits = 15, decimal_places = 10)
    location = models.CharField(max_length = 200)

    created_at = models.DateTimeField('date created', auto_now_add = True)
    updated_at = models.DateTimeField('date updated', auto_now = True)

    attachments = models.ManyToManyField(Attachment, blank = True)

    def __unicode__(self):
        return self.title

tagging.register(Issue)

# horrible hack for failing tags overwrite
from tagging.models import Tag
Tag.name_any = property(lambda self: self.name)
