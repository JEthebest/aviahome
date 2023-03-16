from django.contrib import admin

from .models import Airport


@admin.register(Airport)
class FoodAdmin(admin.ModelAdmin):
    pass