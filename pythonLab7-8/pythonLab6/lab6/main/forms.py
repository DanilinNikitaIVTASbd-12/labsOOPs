from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Visitors, Orders, Bank, Employees, Intermediary
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput, CheckboxInput, Select, SelectMultiple, PasswordInput


class VisitorsForm(ModelForm):
    class Meta:
        model = Visitors
        fields = ['name', 'gender', 'date', 'online']

        widgets = {
            "name": TextInput(attrs={
                'placeholder': 'Имя пользователя'
            }),

            "gender": TextInput(attrs={
                'placeholder': 'Пол пользователя'
            }),

            "date": DateTimeInput(attrs={
                'placeholder': 'DD.MM.HHHH HH:MM:SS'
            }),

            "online": CheckboxInput(attrs={
                'placeholder': 'Онлайн'
            }),
        }


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


class BankForm(ModelForm):
    class Meta:
        model = Bank
        fields = ['name', 'address', 'square']

        widgets = {
            "name": TextInput(attrs={
                'placeholder': 'Название банка'
            }),

            "address": TextInput(attrs={
                'placeholder': 'Месторасположение банка'
            }),

            "square": NumberInput(attrs={
                'placeholder': 'Рейтинг банка'
            })
        }


class EmployeesForm(ModelForm):
    class Meta:
        model = Employees
        fields = ['bankId', 'name', 'gender', 'position', 'salary']

        widgets = {
            "bankId": Select(attrs={
                'placeholder': 'Номер банка'
            }),

            "name": TextInput(attrs={
                'placeholder': 'Имя сотрудника'
            }),

            "gender": TextInput(attrs={
                'placeholder': 'Пол сотрудника'
            }),

            "position": TextInput(attrs={
                'placeholder': 'Должность сотрудника'
            }),

            "salary": NumberInput(attrs={
                'placeholder': 'Заработная плата сотрудника'
            })
        }


class IntermediaryForm(ModelForm):
    class Meta:
        model = Intermediary
        fields = ['customerId', 'product', 'time', 'guarantee']

        widgets = {
            "customerId": SelectMultiple(attrs={
                'placeholder': 'Номера банков'
            }),

            "product": TextInput(attrs={
                'placeholder': 'Категория перевода'
            }),

            "time": NumberInput(attrs={
                'placeholder': 'Сроки перевода'
            }),

            "guarantee": CheckboxInput(attrs={
                'placeholder': 'Гарантия'
            })
        }


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            "username": TextInput(attrs={
                'placeholder': 'Имя пользователя'
            }),

            "password1": PasswordInput(attrs={
                'placeholder': 'Пароль'
            }),

            "password2": PasswordInput(attrs={
                'placeholder': 'Подтверждение пароля'
            })
        }