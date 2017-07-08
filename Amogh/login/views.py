from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import LoginForm,SignupForm

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Response')

        else:
            form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_signup(request):
    user_form = SignupForm()
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
            user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponse("Signup Success")
        else:
            user_form = SignupForm()
    return render(request,
                      'signup.html',
                      {'form': user_form})


