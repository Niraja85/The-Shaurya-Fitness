from django.db import models
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    """Defines categories to apply to products.
    A simple model to group products."""

    category_name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """Defines the Product Class. Many fields are optional.
    A default image is uploaded if no image is selected.
    Images will be resized on upload to 500x500px square shape.
    I would recommend cropping your images to a 1:1 ratio first."""

    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images',)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_name












