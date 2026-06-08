from django.contrib import admin
from .models import Products

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'price']
    list_filter = ['color', 'model']
    search_fields = ['name', 'model']
# Register your models here.
