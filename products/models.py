from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
# Create your models here.


class Category(models.Model):
    """Defines categories to apply to products.
    A simple model to group products."""

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Defines the Product Class. Many fields are optional.
    A default image is uploaded if no image is selected.
    Images will be resized on upload.I would recommend cropping your images
    to a 1:1 ratio first."""

    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=500, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
