
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings

from models import Institution

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
    return render_to_response('institutions/view.html',
        context_instance=RequestContext(request, {'institution': institution}))
