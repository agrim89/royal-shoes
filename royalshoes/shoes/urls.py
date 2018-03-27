from rest_framework import routers
from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.RegisterViewSet.as_view(), name='register'),
    path('login/', views.ValidateViewSet.as_view(), name='validate'),
    path('company_detail/', views.CompanyDetailViewSet.as_view(), name='company_detail'),
    path('shoes/', views.ShoesViewSet.as_view(), name='shoes_list'),
    path('cart/', views.AddToCartViewSet.as_view(), name='add_to_cart'),
]
