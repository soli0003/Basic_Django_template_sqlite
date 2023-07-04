from . import views
from django.urls import path
from .views import products_view, TokenObtainPairView

urlpatterns = [
    path('products', products_view.as_view()),
    path('products/<str:category>', products_view.as_view(), name='products_by_category'),
    path('login', TokenObtainPairView.as_view()),
    path('register', views.register),
    path('index', views.index),

]