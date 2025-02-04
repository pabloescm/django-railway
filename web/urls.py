from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'category', views.CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('articles/', views.render_articles, name='articles'),
]
