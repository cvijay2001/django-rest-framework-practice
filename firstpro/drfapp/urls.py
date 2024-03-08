from django.contrib import admin
from django.urls import path,include
from drfapp import urls
from . import views

urlpatterns = [
    path('studentinfo/<int:pk>/', views.home, name='home'),
    path('studentinfo', views.home, name='home'),
]
