from django.urls import path
from . import views

urlpatterns = [
    # path('student_create/<int:pk>/', views.student_create, name='student_create'),
    path('student_create', views.student_create, name='student_create'),
    path('get_student', views.get_student, name='get_student'),
    
]
