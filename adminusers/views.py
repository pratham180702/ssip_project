from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import AdminUsers
from .forms import AdminRegister
#added now
from django.contrib import messages
# added 2

# Create your views here.

def admin_register(request):
    if request.method=='POST':
        form = AdminRegister(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = AdminRegister()
    context = {
                'form' : form,
                'title' : 'Register'
              }
    return render(request,'adminregister.html',context)
