from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)