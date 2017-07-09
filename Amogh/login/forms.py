from django.contrib.auth.models import User
from django.core.validators import validate_email

from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirmpassword = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User

        fields = ('username', 'first_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data

            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']



