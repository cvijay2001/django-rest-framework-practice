from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='Gsignupapp/home.html'), name='home'),
    path('login', TemplateView.as_view(template_name='account/login.html'), name='login'),
    path('login', TemplateView.as_view(template_name='Gsignupapp/login_user.html'), name='login_user'),

    path('accounts/', include('allauth.urls')),
    path('', views.home,name='home'),
]