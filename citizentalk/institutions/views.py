
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings

from tagging.models import TaggedItem
from citizentalk.issues.models import Issue

from models import Institution, HoldingOffice

def search(request):
    try:
        page = int(request.GET.get('page', '1'))
    except (ValueError, TypeError):
        page = 1

    all_institutions = Institution.objects.all()
    try:
        institutions = Paginator(all_institutions, \
            settings.ITEMS_PER_PAGE).page(page)
    except (EmptyPage, InvalidPage):
        raise Http404

    return render_to_response('institutions/search.html',
        context_instance = RequestContext(request, 
            {'institutions': institutions}))

def view(request, id):
    institution = get_object_or_404(Institution, pk=id)
    print 
    for tag in institution.tags.split():
        if tag.startswith('location:'):
            issues = TaggedItem.objects.get_by_model(Issue, tag)
            break
    else:
        issues = []

    people_in_office = HoldingOffice.objects.filter(institution=institution,
                                                    end_date=None)
    if people_in_office:
        person_in_office = people_in_office[0].person
    else:
        person_in_office = None

    return render_to_response('institutions/view.html',
        context_instance=RequestContext(request, {
            'institution': institution,
            'issues': issues,
            'person_in_office': person_in_office,
        }))
