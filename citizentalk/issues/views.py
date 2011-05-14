
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

from forms import CreateForm

def index(request):
    return render_to_response('issues/index.html',
        context_instance = RequestContext(request))

@login_required
def new(request):
    form = CreateForm()
    return render_to_response('issues/new.html',
        {'form': form},
        context_instance = RequestContext(request))

