from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True, help_text='unique page name created from product name')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/categories/', blank=True)
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255, blank=True, help_text='Comma-delimited set of SEO keywords for meta tags')
    meta_description = models.CharField("Meta Description", max_length=255, blank=True, help_text='Content for description meta tag') #the meta description string is the verbose name that will be used to represent the field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_category', kwargs={'category_slug': self.slug})

