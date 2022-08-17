from django import forms

from .models import Member


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        exclude = ['slug', 'church']
        labels = {
            'fullName': 'Nome Completo',
            'cpf': 'CPF',
            'adress': 'Endereço',
            'genre': 'Gênero',
            'phone': 'Telefone',
            'born': 'Nascimento',
            'emai': 'Email',
            'number': 'Nº',
            'genre': 'Gênero',
            'city': 'Cidade',
            'state': 'Estado',
            'district': 'Bairro',
            'is_baptized_water': 'Batizado nas águas',
            'is_baptized_holySpirit': 'Batizado no Espírito Santo',
            'is_tither': 'Dizimista',
            'upload': 'Imagem',
        }

        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Telefone', 'data-mask': '(99) 99999-9999'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'CNPJ da empresa', 'data-mask': '000.000.000-00', 'minlength': '14'}),  # noqa
            'state': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Estado'}),  # noqa
            'genre': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gênero'}),  # noqa
            'upload': forms.FileInput(attrs={'placeholder': 'Arquivo de Imagem'}),  # noqa
        }
