
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from django.contrib.comments.models import Comment

from issues.models import Issue

def index(request):
    reported_issues = Issue.objects.all().count()
    fixed_issues = Issue.objects\
        .filter(Q(state = u'res') | Q(state = u'acc')).count()
    updates_on_reports = Comment.objects.all().count()

    return render_to_response('dashboard/index.html',
        {'reported_issues': reported_issues, 'fixed_issues': fixed_issues,
         'updates_on_reports': updates_on_reports},
        context_instance = RequestContext(request))

