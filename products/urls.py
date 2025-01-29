from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('create/', views.product_create, name='create'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.product_detail, name='detail'),
]