
from django.shortcuts import render_to_response
from django.template import RequestContext

from profiles.forms import JoinForm

def join(request):

    return render_to_response('profiles/join.html',
        {'form': JoinForm()},
        context_instance = RequestContext(request))

