import re

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError

from .models import Church



class ChurchFormAdmin(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ChurchFormAdmin, self).__init__(*args, **kwargs)
        self.fields['cnpj'].widget.attrs['class'] = 'mask-cnpj'
        self.fields['phone'].widget.attrs['class'] = 'mask-phone'

    def clean_email(self):
        data = self.cleaned_data.get('email')
        print('CNPJ VALIDACAO ENTROu', data)
        if Church.objects.filter(email=data).count() > 1:
            return ValidationError(
                'Email existente',
                code='Already_exists'
            )
        else:
            return data

    def clean_cnpj(self):
        data = self.cleaned_data.get('cnpj')
        print('CNPJ VALIDACAO ENTROu', data)
        if Church.objects.filter(cnpj=data).exists():
            if Church.objects.filter(cnpj=data).count() > 1:
                return ValidationError(
                    'CNPJ existente',
                    code='Already_exists'
                )
        elif len(data) < 18:
            return ValidationError(
                'CNPJ com tamanho invalido',
                code='invalid_size'
            )

        return data
