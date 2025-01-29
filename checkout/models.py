from django.db import models
from django import forms
from products.models import Product
from django.core.validators import RegexValidator

class Order(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    street_address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    credit_card_number = models.CharField(
        max_length=19,
        validators=[RegexValidator(r'^\d{16,19}$', 'Credit card number must be 16-19 digits only')]
    )
    expiry_date = models.CharField(
        max_length=5,
        validators=[RegexValidator(r'^\d{2}/\d{2}$', 'Format should be MM/YY')]
    )
    cvv = models.CharField(
        max_length=4,
        validators=[RegexValidator(r'^\d{3,4}$', 'CVV should be 3 or 4 digits only')]
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Order {self.pk}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.pk)

    def get_cost(self):
        return self.price * self.quantity

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'street_address', 'city', 'postal_code', 'credit_card_number', 'expiry_date', 'cvv']