from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm
from django import forms

from .models import CustomUser



# class CustomCreate(UserCreationForm, ModelForm):

#     password1 = forms.CharField(label='Password', 
#                                 widget=forms.PasswordInput(attrs={
#                                     'placeholder':'password',
#                                     }))
#     password2 = forms.CharField(label='Password Confirmation', 
#                                 widget=forms.PasswordInput(attrs={
#                                     'placeholder':'Password Confirmation',
#                                     }))

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder':'Username'}),
#             'email': forms.TextInput(attrs={'placeholder':'Email'}),
#         }


# class CustomChange(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = UserChangeForm.Meta.fields
