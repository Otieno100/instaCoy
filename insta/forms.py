from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django import forms
from django.contrib.auth.models import User
# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

class InstaLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')