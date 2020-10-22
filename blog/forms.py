from django import forms
import django.forms.widgets

class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True}))
