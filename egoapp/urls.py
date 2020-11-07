from django.contrib import admin
from django.urls import path
from .views import *
from egoapp import views

urlpatterns = [
    path('store',views.store),
    path('checkout',views.checkout),
    path('cart',views.cart,name="cart"),

]
