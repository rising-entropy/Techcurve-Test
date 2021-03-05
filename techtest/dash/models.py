from django.db import models
# Create your models here.
from django.db.models import OneToOneField

class Expenses(models.Model):
    date = models.DateField()
    #True -> Yes, False -> No
    isBOIsalary = models.BooleanField(default=False)
    amount = models.IntegerField()

class Invoice(models.Model):
    customerName = models.CharField(max_length=255)
    invoiceNumber = models.CharField(max_length=255)
    amount = models.IntegerField()
    invoiceDate = models.DateField()
    paymentDate = models.DateField(null=True)
    # True -> paid, False -> due
    state = models.BooleanField(default=False)
    
class Revenues(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE)
    dateReceived = models.DateField()