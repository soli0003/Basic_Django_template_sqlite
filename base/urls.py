from . import views
from django.urls import path
from .views import products_view, TokenObtainPairView
from rest_framework_simplejwt.views import ( TokenRefreshView)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # path('addCategory', views.addCategory),
    path('products', products_view.as_view()),
    path('products/<int:pk>', products_view.as_view()),
    path('products/<str:category>', products_view.as_view(), name='products_by_category'),
    path('login', views.MyTokenObtainPairView.as_view()),
    path('logout', LogoutView.as_view(), name='logout'),
    path('refresh', TokenRefreshView.as_view()),
    path('register', views.register),
    path('index', views.index),
    
]