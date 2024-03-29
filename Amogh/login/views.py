from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
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
                    return redirect(level1)
                else:
                    return redirect(error_view)
            else:
                return redirect(error_view)

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
            return render(request,'signupsuccess.html')
        else:
            user_form = SignupForm()
    return render(request,
                      'signup.html',
                      {'form': user_form})

def admin_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(level1)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Response')

        else:
            form = LoginForm()
    return render(request, 'login.html', {'form': form})

def admin_signup(request):
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
                      'AdminSignup.html',
                      {'form': user_form})




@login_required
def logout_view(request):
    logout(request)
    return HttpResponse("Logout Successful")

@login_required
def level1(request):
    return render(request,'t1.html')

@login_required
def level2(request):
    return  render(request,'t2.html')

@login_required
def level3(request):
    return render(request,'seminar_form.html')

@login_required
def level4(request):
    return render(request,'form_4.html')

@login_required
def level5(request):
    return render(request,'t5.html')


def error_view(request):
    return render(request,'error.html')