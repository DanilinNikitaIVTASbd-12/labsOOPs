from .models import Orders
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput


class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['visitorNumber', 'title', 'price', 'date']

        widgets = {
            "title": TextInput(attrs={
                'placeholder': 'Категория перевода'
            }),

            "price": NumberInput(attrs={
                'placeholder': 'Сумма перевода'
            }),

            "date": DateTimeInput(attrs={
                'placeholder': 'DD.MM.HHHH HH:MM:SS'
            })
        }
