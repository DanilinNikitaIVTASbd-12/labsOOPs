from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Visitors, Orders, Bank, Employees, Intermediary
from .forms import VisitorsForm, OrdersForm, BankForm, EmployeesForm, IntermediaryForm, RegisterUserForm
from django.views.generic import UpdateView, DeleteView, CreateView


def index(request):
    visitorsTable = Visitors.objects.all()
    ordersTable = Orders.objects.all()
    bankTable = Bank.objects.all()
    employeesTable = Employees.objects.all()
    intermediaryTable = Intermediary.objects.all()

    form = OrdersForm()

    if request.method == 'POST':
        form = OrdersForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')

    return render(request, 'main/index.html', {'visitors': visitorsTable, 'orders': ordersTable, 'bank': bankTable, 'employees': employeesTable, 'intermediary': intermediaryTable, 'form': form})


class VisitorsUpdateView(UpdateView):
    model = Visitors
    template_name = 'main/visitor-update.html'

    form_class = VisitorsForm


class OrdersUpdateView(UpdateView):
    model = Orders
    template_name = 'main/order-update.html'

    form_class = OrdersForm


class OrdersDeleteView(DeleteView):
    model = Orders
    template_name = 'main/order-delete.html'
    success_url = '/'


class BankUpdateView(UpdateView):
    model = Bank
    template_name = 'main/bank-update.html'

    form_class = BankForm


class EmployeesUpdateView(UpdateView):
    model = Employees
    template_name = 'main/employee-update.html'

    form_class = EmployeesForm


class IntermediaryUpdateView(UpdateView):
    model = Intermediary
    template_name = 'main/intermediary-update.html'

    form_class = IntermediaryForm

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')