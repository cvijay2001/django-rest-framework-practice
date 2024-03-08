from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'ViewsetApp'
router = DefaultRouter()

router.register(r'StudentAPI', views.StudentViewset, basename='studentapi')

urlpatterns = [
    path('',include(router.urls)),
]
