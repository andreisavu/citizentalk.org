
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import Http404

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required
from django.conf import settings

from tagging.models import Tag, TaggedItem

from issues.models import Issue, Attachment
from issues.forms import CreateForm, CreateAttachmentForm
from institutions.models import Institution

def index(request):
    if request.method == 'GET':
        return list_issues(request)
    elif request.method == 'POST':
        return create(request)

def view(request, id):
    issue = get_object_or_404(Issue, pk=id)
    issue_attachments = issue.attachments.all()
    institutions = TaggedItem.objects.get_by_model(Institution, issue.tags)[:5]
    attachment_form = CreateAttachmentForm()

    return render_to_response('issues/view.html',
        {'issue': issue, 'issue_attachments': issue_attachments,
        'institutions': institutions, 'form': attachment_form },
        context_instance = RequestContext(request))

@login_required
def new(request):
    form = CreateForm()
    return render_to_response('issues/new.html',
        {'form': form},
        context_instance = RequestContext(request))

@login_required
def create(request):
    form = CreateForm(request.POST)

    if form.is_valid():
        issue = create_issue(request)
        issue.save()
        return redirect('/issues/')
    else:
        return render_to_response('issues/new.html',
            {'form': form},
            context_instance = RequestContext(request))

@login_required
def add_attachment(request, id):
    issue = get_object_or_404(Issue, pk=id)
    issue_attachments = issue.attachments.all()
    institutions = TaggedItem.objects.get_by_model(Institution, issue.tags)[:5]
    attachment_form = CreateAttachmentForm(request.POST, request.FILES)

    if attachment_form.is_valid():
        attachment = create_attachment(request, issue)
        attachment.save()
        return redirect('/issues/view/' + str(issue.id))
    else:
        return render_to_response('issues/view.html',
            {'issue': issue, 'issue_attachments': issue_attachments,
            'institutions': institutions, 'form': attachment_form },
            context_instance = RequestContext(request))
    

def list_issues(request):
    try:
        page = int(request.GET.get('page','1'))
    except (ValueError, TypeError):
        page = 1

    all_issues = Issue.objects.order_by('-created_at') 
    try:
        issues = Paginator(all_issues, settings.ITEMS_PER_PAGE).page(page)
    except (EmptyPage, InvalidPage):
        raise Http404

    return render_to_response('issues/index.html',
        {'issues': issues},
        context_instance = RequestContext(request))

def create_attachment(request, issue):
    return issue.attachments.create(title = request.POST['title'],
        file = request.FILES['file'])

def create_issue(request):
    return Issue(title = request.POST['title'],
        description = request.POST['description'],
        latitude = request.POST['latitude'],
        longitude = request.POST['longitude'],
        tags = request.POST['tags'],
        reporter = request.user)
