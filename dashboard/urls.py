from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('starter', views.starter_view),
]
