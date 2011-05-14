from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages

from models import Institution
from forms import InstitutionForm

def search(request):
    results = Institution.objects.all()
    return render_to_response('institutions/search.html',
        context_instance = RequestContext(request, {'institutions': results}))

def edit(request):
    institution = get_object_or_404(Institution, pk=request.GET['id'])

    if request.POST:
        form = InstitutionForm(request.POST, instance=institution)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,
                                 "%s saved." % institution.title)

    else:
        form = InstitutionForm(instance=institution)

    return render_to_response('institutions/edit.html',
        context_instance = RequestContext(request, {'form': form}))
