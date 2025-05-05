from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, SubCategory

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'description', 'expected_price_range', 'category']


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class WorkerSignupForm(UserCreationForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())  # Updated to allow multiple selections


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'categories']  # Updated field name


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
