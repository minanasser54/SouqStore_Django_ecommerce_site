from django.contrib import admin
from django.urls import path
from . import views

app_name="accounts"

urlpatterns=[
    path('signup/',views.signup,name="signup"),
    path('<slug:slug>/',views.profile,name="profile"),
]
