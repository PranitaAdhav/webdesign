from django import forms
from .models import blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())


class blog_form(forms.ModelForm):
    class Meta:
        model = blog
        fields = '__all__'

    title = forms.CharField(widget=forms.TextInput({'placeholder':'enter a title'}))
    content = forms.CharField(widget=forms.TextInput({'placeholder':'enter a content'}))
    img_1 = forms.ImageField()
    date = forms.DateField(widget=forms.TextInput({'placeholder':'enter a date'}))
    