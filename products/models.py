from django.db import models
from django.utils.text import slugify
from catalogs.models import Catalog
from django.urls import reverse



class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='products')
    product_image = models.ImageField(upload_to='product_images/')
    quantity = models.PositiveIntegerField()
    sizes = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)


    def get_detail_url(self):
        return reverse(
            'products:detail',
            kwargs={
                'year': self.created_at.year,
                'month': self.created_at.month,
                'day': self.created_at.day,
                'slug': self.slug,
            })
