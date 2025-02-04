from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_articles, name='articles'),
    path('category/', views.CategoriaViewSet, name='category'),
]
