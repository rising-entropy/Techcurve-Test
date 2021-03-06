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

router4 = DefaultRouter()
router4.register('bankbalance', BankBalanceViewSet, basename='bankbalance')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/', include(router2.urls)),
    path('viewset/', include(router3.urls)),
    path('viewset/', include(router4.urls)),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/profitloss/', ProfitLoss.as_view(), name='ProfitLoss'),
    path('api/currentbankbalance/', CurrentBankBalance.as_view(), name='CurrentBankBalance'),
    path('api/monthlyexpensesummary/', MonthlyExpensesSummary.as_view(), name='MonthlyExpensesSummary'),
    path('api/monthlyplsummary/', MonthlyPLSummary.as_view(), name='MonthlyPLSummary'),
    path('api/profitlossgraph/', ProfitLossGraph.as_view(), name='ProfitLossGraph'),
    path('api/expense/', Expense.as_view(), name='Expense'),
    path('api/revenue/', Revenue.as_view(), name='Revenue'),
    path('api/invoices/', AllInvoices.as_view(), name='AllInvoices'),
    path('api/monthlyrevenue/<int:year>/<int:month>', MonthlyRevenue.as_view(), name='MonthlyRevenue'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/revenuebymonth/<int:year>/<int:month>', RevenueByMonth.as_view(), name='RevenueByMonth'),
    path('api/expensebymonth/<int:year>/<int:month>', ExpenseByMonth.as_view(), name='ExpenseByMonth'),
    path('api/profitlossbymonth/<int:year>/<int:month>', PLByMonth.as_view(), name='PLByMonth'),
]