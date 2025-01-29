from django.shortcuts import render, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.models import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return redirect('checkout:checkout-success', order_id=order.id)
    else:
        form = OrderCreateForm()

    return render(request, 'checkout/checkout.html', {'cart': cart, 'form': form})


def checkout_success(request, order_id):
    order = Order.objects.get(id=order_id)
    cart = Cart(request)
    return render(request, 'checkout/checkout-success.html', {'order': order, 'cart': cart})

