from django.db import models
from tagging.fields import TagField

class PublicPerson(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Institution(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    tags = TagField()

    def __unicode__(self):
        return self.title


class HoldingOffice(models.Model):
    person = models.ForeignKey(PublicPerson)
    institution = models.ForeignKey(Institution)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return (u"%(person)s - %(office)s "
                u"from %(start_date)s to %(end_date)s") % {
            'person': self.person.name,
            'office': self.institution.title,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date or "present"),
        }
