import re

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError

from .models import Account


class AccountUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        exclude = ('password', 'senha', 'is_admin', 'is_active', 'is_staff',
                   'is_superuser', 'last_login',)


class AccountForm(UserChangeForm):
    password = None

    class Meta:
        model = Account
        fields = '__all__'

        




    
