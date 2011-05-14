from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Institution

def search(request):
    results = Institution.objects.all()
    return render_to_response('institutions/search.html',
        context_instance = RequestContext(request, {'institutions': results}))
