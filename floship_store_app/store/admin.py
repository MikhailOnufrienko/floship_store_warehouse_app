from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Order


@register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.get_fields()]

