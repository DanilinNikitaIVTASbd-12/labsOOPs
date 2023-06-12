from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),

    path('visitors/<int:pk>/update', views.VisitorsUpdateView.as_view(), name='visitor-update'),
    path('orders/<int:pk>/update', views.OrdersUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete', views.OrdersDeleteView.as_view(), name='order-delete'),
    path('bank/<int:pk>/update', views.BankUpdateView.as_view(), name='bank-update'),
    path('employees/<int:pk>/update', views.EmployeesUpdateView.as_view(), name='employee-update'),
    path('intermediary/<int:pk>/update', views.IntermediaryUpdateView.as_view(), name='intermediary-update'),

    path('registration', views.RegisterUser.as_view(), name='registration'),
    path('authorization', views.LoginUser.as_view(), name='authorization'),
    path('exit', views.logout_user, name='exit')
]
