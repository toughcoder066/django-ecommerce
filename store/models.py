from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, help_text='unique value for product page url, created from product name')
    brand = models.CharField(max_length=50, blank=True)
    sku = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    image = models.ImageField(upload_to='photos/products/', blank=True)
    is_available = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length=255, blank=True, help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)

    class Meta:
        db_table = 'Products'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        first_category = self.category.first() #this selects the first category from the many to many
        return reverse('product_detail', kwargs={'category_slug':first_category.slug,'product_slug': self.slug})
    
    def sale_price(self):
        return self.price if self.old_price > self.price else None
    