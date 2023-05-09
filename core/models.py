from django.utils import timezone
from django.db import models


class Employee(models.Model):
    surname = models.CharField(max_length=50, null=False, blank=True)
    name = models.CharField(max_length=50, null=False, blank=True)
    otchestvo = models.CharField(max_length=50, null=True, blank=True)


class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='order')
    departure = models.CharField(max_length=50, null=False, blank=True)
    destination = models.CharField(max_length=50, null=False, blank=True)
    date = models.DateField(default=timezone.now(), blank=True)


class Client(models.Model):
    surname = models.CharField(max_length=50, null=False, blank=True)
    name = models.CharField(max_length=50, null=False, blank=True)
    otchestvo = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=False, blank=True)
    order = models.ManyToManyField(Order)
