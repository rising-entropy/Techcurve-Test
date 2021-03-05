
from django.urls import path, include
from .views import article_list, article_detail, ArticleList, ArticleDetail, GenericArticleList, GenericArticleDetail, GenericViewSetOP
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', GenericViewSetOP, basename='article')

urlpatterns = [
    
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    #path('article/', article_list),
    path('article/', ArticleList.as_view()),
    #path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetail.as_view()),
    path('generic/article/', GenericArticleList.as_view()),
    path('generic/detail/<int:id>/', GenericArticleDetail.as_view()),
]
