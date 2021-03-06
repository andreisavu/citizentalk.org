
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class JoinForm(UserCreationForm):
    email = forms.EmailField(required = True)

def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            User.objects.create_user(form.cleaned_data['username'], 
                form.cleaned_data['email'], form.cleaned_data['password1'])
            return redirect('/login')
    else:
        form =JoinForm()

    return render_to_response('profiles/join.html',
        {'form': form},
        context_instance = RequestContext(request))

