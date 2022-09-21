# flake8: noqa: E501
import datetime

from churchManager import settings
from django import forms
from django.core.exceptions import ValidationError

from .models import Entrie


class EntrieForm(forms.ModelForm):
    date = forms.DateField(label="Data", required=False, input_formats=settings.DATE_INPUT_FORMATS,
                           widget=forms.DateInput(format="%d/%m/%Y", attrs={'readOnly': False, 'id': 'startLocationID', 'data-mask': '99/99/9999'}))

    class Meta:
        model = Entrie
        fields = '__all__'

        labels = {
            'category': 'Categoria',
            'value': 'Valor(R$)',
            'ocassion': 'Ocasião',
            'church': 'church'
        }

        widgets = {
            'id': forms.HiddenInput(),
            'category': forms.Select(attrs={'placeholder': 'Categoria', 'class': 'form-control'}),  # noqa
            'church': forms.HiddenInput(),
            'value': forms.NumberInput(attrs={'placeholder': ' Valor', 'required': 'True'}),  # noqa
            'ocassion': forms.TextInput(attrs={'placeholder': 'Ex: Dízimo da ad Acampamento'})

        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        hoje = datetime.date.today()
        if date == None or len(date) == 0:
            date = hoje

        if date > hoje or date.month != hoje.month:
            raise ValidationError((
                'Data indisponivel'
            ),
                code='invalid'
            )
        return date
