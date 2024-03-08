from django.contrib import admin
from django.urls import path
from .views import ListCreateStudentAPI,RUDStudentAPI

urlpatterns = [
    path('ListCreateStudentAPI/',ListCreateStudentAPI.as_view(),name='lc'),
    path('RUDStudentAPI/<int:pk>',RUDStudentAPI.as_view(),name='rud'),
]
