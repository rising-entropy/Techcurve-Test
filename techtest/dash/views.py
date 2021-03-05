from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
import json

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    
class RevenuesViewSet(viewsets.ModelViewSet):
    serializer_class = RevenuesSerializer
    queryset = Revenues.objects.all()
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    
class ExpensesViewSet(viewsets.ModelViewSet):
    serializer_class = ExpensesSerializer
    queryset = Expenses.objects.all()
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    
class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    
class ProfitLoss(APIView):
    
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    
    def get(self, request):
        profitLossValue = 0
        allExpenses = Expenses.objects.all()
        for i in allExpenses:
            profitLossValue -= i.amount
        allRevenues = Revenues.objects.all()
        for i in allRevenues:
            profitLossValue += i.invoice.amount
        
        value = {
            'profitOrLoss': profitLossValue
        }
        
        return JsonResponse(value)
    
class Revenue(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    
    def get(self, request):
        totalRevenue = 0
        
        allRevenues = Revenues.objects.all()
        for i in allRevenues:
            totalRevenue += i.invoice.amount
            
        value = {
            'totalRevenue': totalRevenue
        }
        
        return JsonResponse(value)
    
class Expense(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    
    def get(self, request):
        totalExpense = 0
        
        allExpenses = Expenses.objects.all()
        for i in allExpenses:
            totalExpense += i.amount
            
        value = {
            'totalExpense': totalExpense
        }
        
        return JsonResponse(value)
    
    
class AllInvoices(generics.GenericAPIView, mixins.ListModelMixin):
    
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return self.list(request)
    

class MonthlyRevenue(APIView):
    
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    
    def get(self, request, year, month):
        try:
            article = Revenues.objects.all().filter()
            article2 = []
            for i in article:
                if i.dateReceived.month == month and i.dateReceived.year == year:
                    article2.append(i)
            monthlyRev = []
            c=1
            for i in article2:
                letsHaveAJSON = {}
                letsHaveAJSON["id"] = i.id
                letsHaveAJSON["dateReceived"] = i.dateReceived
                letsHaveAJSON["customerName"] = i.invoice.customerName
                letsHaveAJSON["invoiceNumber"] = i.invoice.invoiceNumber
                letsHaveAJSON["amount"] = i.invoice.amount
                letsHaveAJSON["invoiceDate"] = i.invoice.invoiceDate
                letsHaveAJSON["paymentDate"] = i.invoice.paymentDate
                letsHaveAJSON["state"] = i.invoice.state
                monthlyRev.append(letsHaveAJSON)
                c += 1         
        except Revenues.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(monthlyRev)

class MonthlyPLSummary(APIView):
    
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            #all Months ke revenues
            article = Revenues.objects.all()
            article2 = {}
            for i in article:
                thatYear = i.dateReceived.year
                thatMonth = i.dateReceived.month
                thatCombo = tuple([thatYear, thatMonth])
                if thatCombo not in article2.keys():
                    article2[thatCombo] = []
                    article2[thatCombo].append(i.invoice.amount)
                else:
                    article2[thatCombo][0] += i.invoice.amount
            for i in article2.values():
                i.append(0)
            article = Expenses.objects.all()
            for i in article:
                thatYear = i.date.year
                thatMonth = i.date.month
                thatCombo = tuple([thatYear, thatMonth])
                if thatCombo not in article2.keys():
                    article2[thatCombo] = []
                    article2[thatCombo].append(0)
                    article2[thatCombo].append(i.amount)
                else:
                    article2[thatCombo][1] += i.amount
            monthlyRev = []
            c = 1
            for k, v in article2.items():
                lemmeGetThatJson = {
                    'id': c,
                    'year': k[0],
                    'month': k[1],
                    'revenue': v[0],
                    'expense': v[1],
                    'profit': v[0] - v[1]
                }
                c+=1
                monthlyRev.append(lemmeGetThatJson)
        except Revenues.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(monthlyRev)