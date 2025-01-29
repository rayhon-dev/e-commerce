from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('success/<int:order_id>/', views.checkout_success, name='checkout-success'),
]