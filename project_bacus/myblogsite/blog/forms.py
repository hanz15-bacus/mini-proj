from django import forms

from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username',required=True, max_length=20)
    email = forms.EmailField(label='Email', required=True, max_length=254)  
    age = forms.IntegerField(label='Age')
    password = forms.CharField(label='Password',required=True, max_length=100, widget=forms.PasswordInput())
    confpassword = forms.CharField(label='Confirm Password', required=True, max_length=100, widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',required=True, max_length=20)
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput())  
