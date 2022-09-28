
# flake8: noqa: E501
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError

from .models import Church


class ChurchForm(UserChangeForm):
    password = None

    class Meta:
        model = Church
        fields = ['email', 'name', 'ministery',
                  'cnpj', 'phone', 'number',
                  'adress', 'district',
                  'city', 'state']

        labels = {
            'email': 'email',
            'ministery': 'Ministério',
            'number': 'Nº',
            'name': 'Nome',
            'cnpj': 'CNPJ',
            'phone': 'Telefone',
            'adress': 'Endereço',
            'district': 'Bairro',
            'city': 'Cidade',
            'state': 'Estado',

        }

        widgets = {
            'cnpj': forms.TextInput(attrs={'placeholder': 'CNPJ da igreja', 'data-mask': '99.999.999/9999-99'}),  # noqa
            'name': forms.TextInput(attrs={'placeholder': ' Nome da igreja', 'required': 'True'}),  # noqa
            'phone': forms.TextInput(attrs={'placeholder': ' Telefone', 'data-mask': '(99) 99999-9999'}),  # noqa
            'email': forms.EmailInput(attrs={'placeholder': 'Email da igreja'}),  # noqa
            'adress': forms.TextInput(attrs={'placeholder': 'Endereço da igreja '}),
            'number': forms.NumberInput(attrs={'placeholder': ' Nº'}),
            'district': forms.TextInput(attrs={'placeholder': 'Bairro da igreja'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'CEP da igreja', 'data-mask': '99999-999'}),  # noqa
            'city': forms.TextInput(attrs={'placeholder': 'Cidade'}),
            'state': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
            'is_admin': forms.HiddenInput(),
            'is_active': forms.HiddenInput(),
            'is_staff': forms.HiddenInput(),
            'is_superuser': forms.HiddenInput(),
            'password': forms.HiddenInput(),
            'last_login': forms.HiddenInput(),
        }

    def clean_phone(self):
        number = self.cleaned_data.get('phone')
        print(number)

        if len(number) < 15 or number is None:
            raise ValidationError((
                'Telefone Invalido'
            ),
                code='invalid'
            )
        return number


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
