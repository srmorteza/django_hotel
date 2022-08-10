from django.contrib import admin

from .models import Property, Category,Reserve


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name','property_type','price','area','beds_number','baths_number','garage_number','category']
    search_fields = ['name','property_type','price']
    list_filter = ['category','property_type']

# Register your models here.
admin.site.register(Property,PropertyAdmin )
admin.site.register(Category)
admin.site.register(Reserve)
