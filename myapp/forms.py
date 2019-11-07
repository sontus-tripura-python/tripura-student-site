from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField()
        first_name = forms.CharField(max_length=30)
        last_name = forms.CharField(max_length=20)
        class Meta:
            model = User
            fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = [
        'photo',
        'title',
        'fathername',
        'mothername',
        'School',
        'college',
        'university',
        'deparment',
        'phone',
        'birthdate',
        'Village',
        'thana',
        'district',
        'current_city',
        'local_city',
        'bio_data',
        ]

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = [
        'photo',
        'title',
        'fathername',
        'mothername',
        'School',
        'college',
        'university',
        'deparment',
        'phone',
        'birthdate',
        'Village',
        'thana',
        'district',
        'current_city',
        'local_city',
        'bio_data',


        ]
