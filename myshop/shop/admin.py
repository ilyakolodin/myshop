from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prtpopulated_fields = {'slug': ('name',)}
    
    
@amin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}