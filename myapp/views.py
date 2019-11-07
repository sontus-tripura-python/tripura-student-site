from django.shortcuts import render , redirect
from .forms import RegistrationForm ,ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
def logout(request):
    return redirect('login')
def tripura(request):
    return render(request, 'blog/home.html')

def profile(request):
    arg = {'user': request.user }
    return render(request, 'blog/profile.html', arg)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
       form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,  request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context  ={
    'p_form': p_form
    }
    return render(request, 'blog/Profile_edit.html', context)

@login_required
def accoount_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context  ={
    'u_form': u_form
    }
    return render(request, 'blog/account.html', context)
