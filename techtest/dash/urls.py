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
    path('api/bankbalance/', BankBalance.as_view(), name='BankBalance'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    #path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]