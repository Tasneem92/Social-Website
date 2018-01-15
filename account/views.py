# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) # Insantiate the form with the submitted data
        if form.is_valid():
            cd = form.cleaned_data
            # Authenticate the user against the databse (User credentials)
            # It returns a User object if authenticated successfully, None otherwise
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)  # Setting the user session
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
    # section variable is used to track which section of the site the user is watching
    # Multiple views may correspond to the same section
