from django.forms import ModelForm
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SingUpForm(UserCreationForm):
    class Meta:
        model= User
        fields=[
            'username',
            'password1',
            'password2',
        ]
        labels={
            'username':'Usuario',
            'password1':'Contraseña',
            'password2':'Vuelva a introducir contraseña',

        }
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }

    def save(self,commit=True):
        user=super(SingUpForm,self).save(commit=False)

        if commit:
            user.save()
        return user
