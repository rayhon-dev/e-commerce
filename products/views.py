from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from catalogs.models import Catalog


def home(request):
    products = Product.objects.all()
    ctx = {'products': products }
    return render(request, 'index.html', ctx)

def product_create(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        product_image = request.FILES.get('product_image')
        quantity = request.POST.get('quantity')
        sizes = request.POST.get('sizes')
        colors = request.POST.get('colors')

        if product_name and description and price and product_image and category and quantity and sizes and colors:
            Product.objects.create(
                product_name=product_name,
                description=description,
                price=price,
                category=Catalog.objects.get(id=category),
                product_image=product_image,
                quantity=quantity,
                sizes=sizes,
                colors=colors
            )
            return redirect('home')
    categories = Catalog.objects.all()
    ctx = {
        'categories': categories
    }

    return render(request, 'products/product-create.html', ctx)


def product_detail(request, year, month, day, slug):
    product = get_object_or_404(
        Product,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day,
    )
    ctx = {'product': product}
    return render(request, 'products/detail.html', ctx)