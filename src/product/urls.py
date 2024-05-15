from django.contrib import admin
from django.urls import path
from . import views

app_name="product"

urlpatterns=[
    path('',views.product_list,name="products"),
    path('<slug:slug>/',views.product_detail,name="product_detail"),
]
