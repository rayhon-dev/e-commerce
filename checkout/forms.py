from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'street_address', 'city',
        'postal_code', 'credit_card_number', 'expiry_date', 'cvv']