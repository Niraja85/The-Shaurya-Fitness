from django.contrib import admin
from .models import Product, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'date_added')
    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)
