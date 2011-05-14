
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('dashboard/index.html',
        context_instance = RequestContext(request))

