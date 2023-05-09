from django.contrib import admin
from core import models


@admin.register(models.Employee)
class Employee(admin.ModelAdmin):
    list_display = ('surname','name')

@admin.register(models.Client)
class Client(admin.ModelAdmin):
    list_display = ('surname','name')

@admin.register(models.Order)
class Order(admin.ModelAdmin):
    list_display = ('departure','destination')