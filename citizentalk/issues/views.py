
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('issues/index.html',
        context_instance = RequestContext(request))

def explore(request):
    return render_to_response('issues/explore.html',
        context_instance = RequestContext(request))

