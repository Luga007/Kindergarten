from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from address.models import Address
from .models import Caretaker


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Caretaker
        fields = ('email', 'password1', 'password2')


    def save(self, commit=True):
        caretaker = super().save(commit=False)
        caretaker.set_password(self.cleaned_data["password1"])
        if commit:
            caretaker.save()
        return caretaker


class UserCreationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'label': 'First Name'}))
    last_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'label': 'Last name'}))
    email = forms.EmailField(max_length=124,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'label': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'label': 'Password'}))
    number = forms.CharField(max_length=20,
                             widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number', 'label':'Numbers'}))
    salary = forms.IntegerField(max_value=1000000,label='Salary',
                                widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Salary'})
    )

    class Meta:
        model = Caretaker
        exclude = ['joined_date', 'address', 'is_admin', 'is_staff', 'is_active']


    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user




class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Caretaker
        exclude = ['password', 'joined_date', 'is_admin', 'is_staff', 'is_active']

