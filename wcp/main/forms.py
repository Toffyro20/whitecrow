from django import forms
from .models import Main
from django.forms import TextInput, DateInput, TimeInput


class MainForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = ['name_c', 'phone_n', 'date_b', 'time_b', 'table_b', 'clients_n']
        widgets = {
            'name_c': TextInput(attrs={
                'class': 'brn_input',
                'placeholder': 'Имя',
            }),
            'phone_n': TextInput(attrs={
                'class': 'brn_input',
                'placeholder': 'Номер телефона',
            }),
            'date_b': DateInput(attrs={
                'class': 'brn_input',
                'placeholder': 'Дата',
            }),
            'time_b': TimeInput(attrs={
                'class': 'brn_input',
                'placeholder': 'Время',
            }),
            'table_b': TextInput(attrs={
                'class': 'brn_input',
                'placeholder': 'Номер стола',
            }),
            'clients_n': TextInput(attrs={
                'class': 'brn_input',
                'placeholder': 'Количество людей',
            }),
        }
