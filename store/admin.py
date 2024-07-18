from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    # form = ProductAdminForm
    
    list_display = ('name', 'price', 'old_price','quantity','updated_at','is_available')
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)

    # sets up slug to be generated from product name
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Product, ProductAdmin)