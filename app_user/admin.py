from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser

# Register your models here.

class AppUserAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','date_joined','last_login','is_active','is_staff','is_superuser',)
    list_display_links = ('email','username')
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        # (None, {
        #     "fields": (
                
        #     ),
        # }),
    )
    

admin.site.register(AppUser, AppUserAdmin)