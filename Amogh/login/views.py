# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import render
from .forms import LoginForm, SignupForm
from .models import User


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.filter(name=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')

                else:
                    return HttpResponse('Disabled account')

            else:
                return HttpResponse('Invalid login')

        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create(name=cd['username'], password=cd['password'], email=cd['email'], isadmin=False, score=0,
                                level=0)
            User.save()
            return HttpResponse('Authenticated successfully')
        else:
            form = SignupForm()
        return render(request, 'signup.html', {'form': form})
