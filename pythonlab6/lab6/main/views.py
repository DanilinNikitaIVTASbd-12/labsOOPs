from django.shortcuts import render
from .models import Visitors, Orders
from .forms import OrdersForm
from django.views.generic import UpdateView, DeleteView


def index(request):
    visitorsTable = Visitors.objects.all()
    ordersTable = Orders.objects.all()
    form = OrdersForm()
    error = ''

    if request.method == 'POST':
        form = OrdersForm(request.POST)

        if form.is_valid():
            form.save()
            form = OrdersForm()
        else:
            error = 'Ошибка в заполнении формы'
            form = OrdersForm()

    return render(request, 'main/index.html', {'visitors': visitorsTable, 'orders': ordersTable, 'form': form, 'error': error})


class OrdersUpdateView(UpdateView):
    model = Orders
    template_name = 'main/order-update.html'

    form_class = OrdersForm


class OrdersDeleteView(DeleteView):
    model = Orders
    template_name = 'main/order-delete.html'
    success_url = '/'