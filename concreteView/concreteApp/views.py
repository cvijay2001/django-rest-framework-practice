from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView, DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import StudentModel
from .serializer import StudentSerializer

class ListCreateStudentAPI(ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

class RUDStudentAPI(RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

