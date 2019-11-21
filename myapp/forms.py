from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]


class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField()
        first_name = forms.CharField(max_length=30)
        last_name = forms.CharField(max_length=20)
        class Meta:
            model = User
            fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
        'photo',
        'title',
        'fathername',
        'mothername',
        'School',
        'birthday',
        'gender',
        'status',
        'college',
        'university',
        'deparment',
        'Village',
        'thana',
        'district',
        'current_city',
        'local_city',
        'religion',
        'Class',
        'current_work',
        'bio_data',




        ]
class ContactForm(forms.Form):
    name = forms.CharField( max_length=30)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
