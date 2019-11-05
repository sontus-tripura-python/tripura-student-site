from django.shortcuts import render , redirect
from .forms import RegistrationForm
# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')

def logout(request):
    messages.info(request, "Logged out successfully!")
    return redirect('login')

def profile(request):
    return render(request, 'blog/profile.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
       form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form })
