from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Expenses)
admin.site.register(Invoice)
admin.site.register(Revenues)
admin.site.register(BankBalance)