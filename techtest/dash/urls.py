from knox import views as knox_views
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('revenues', RevenuesViewSet, basename='revenues')

router2 = DefaultRouter()
router2.register('expenses', ExpensesViewSet, basename='expenses')

router3 = DefaultRouter()
router3.register('invoice', InvoiceViewSet, basename='invoice')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/', include(router2.urls)),
    path('viewset/', include(router3.urls)),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/profitloss/', ProfitLoss.as_view(), name='ProfitLoss'),
    path('api/monthlyplsummary/', MonthlyPLSummary.as_view(), name='MonthlyPLSummary'),
    path('api/expense/', Expense.as_view(), name='Expense'),
    path('api/revenue/', Revenue.as_view(), name='Revenue'),
    path('api/invoices/', AllInvoices.as_view(), name='AllInvoices'),
    path('api/monthlyrevenue/<int:year>/<int:month>', MonthlyRevenue.as_view(), name='MonthlyRevenue'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    #path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]