from django.contrib import admin
from django.urls import path,include
# from viewapi_app import urls
from . import views
urlpatterns = [
    # path('create_student/',views.create_student,name='create_student'),
    path('get_student/',views.get_student,name='get_student'),
    path('get_student/<int:id>/',views.get_student,name='get_student_by_id'),
]
