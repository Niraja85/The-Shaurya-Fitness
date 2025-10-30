from django.contrib import admin
from .models import Product, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'date_added')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)
