from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:pk>/update', views.OrdersUpdateView.as_view(), name='order-update'),
    path('<int:pk>/delete', views.OrdersDeleteView.as_view(), name='order-delete')
]
