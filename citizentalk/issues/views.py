
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('issues/index.html')

def explore(request):
    return render_to_response('issues/explore.html')

