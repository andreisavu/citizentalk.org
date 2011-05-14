
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required

from issues.models import Issue
from issues.forms import CreateForm

def index(request):
    try:
        page = int(request.GET.get('page','1'))
    except (ValueError, TypeError):
        page = 1

    all_issues = Issue.objects.order_by('created_at') 
    try:
        paginator = Paginator(all_issues, 20)
        issues = paginator.page(page).object_list
    except (EmptyPage, InvalidPage):
        raise Http404

    return render_to_response('issues/index.html',
        {'paginator': paginator, 'issues': issues},
        context_instance = RequestContext(request))

@login_required
def new(request):
    form = CreateForm()
    return render_to_response('issues/new.html',
        {'form': form},
        context_instance = RequestContext(request))

