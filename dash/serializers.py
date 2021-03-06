from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import *
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        
class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = "__all__"
        
class RevenuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenues
        fields = ('id', 'invoice', 'dateReceived')
        
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"
        
class BankBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankBalance
        fields = "__all__"