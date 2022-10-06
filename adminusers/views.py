import email
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import forms
from .models import AdminUsers
from .forms import AdminRegister
#added now
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import AdminUsers

from adminusers import forms
# added 2

# Create your views here.

def admin_register(request):
    if request.method=='POST':
        form = AdminRegister(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('mainadmin-login')
    else:
        form = AdminRegister()
    context = {
                'form' : form,
                'title' : 'Register'
              }
    return render(request,'adminregister.html',context)


def login_page(request):
    form = forms.AdminLogin()
    if request.method == 'POST':
        form = forms.AdminLogin(request.POST)
        # if form.is_valid():
        #     user = auth.authenticate(
        #         # username=form.cleaned_data['username'],
        #         email = form.cleaned_data['email'],
        #         password=form.cleaned_data['password'],
        #     )
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            # user = AdminUsers.objects.get(username=username)
            print(user)
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                return redirect('mainadmin-dashboard')
            else:
                message = 'Login failed!'
    return render(request, 'authentication/login.html', context={'form': form})

def dashboard_page(request):
    context = {
        "pk":18
    }
    return render(request, 'admindashboard.html', context)