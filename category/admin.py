from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)
