from django.shortcuts import render , get_object_or_404, redirect
from .forms import RegistrationForm ,ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
# Create your views here.
def logout(request):
    return redirect('login')
def tripura(request):
    return render(request, 'blog/home.html')
def about(request):
    return render(request, 'blog/about.html')
def leadership(request):
    return render(request, 'blog/leadership.html' )
def Membership(request):
    users = User.objects.all()
    context = {'users':users}

    return render(request, 'blog/Membership.html', context)

def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    arg = {'user': user }
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
#this is news section part........
def News_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    context = {'posts': posts}
    return render(request, 'blog/news.html', context)

def news_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = { 'posts':post }
    return render (request, 'blog/news_details.html', context)
