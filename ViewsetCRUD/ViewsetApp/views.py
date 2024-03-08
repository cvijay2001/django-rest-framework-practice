from django.shortcuts import render,get_object_or_404
from .serializer import StudentSerializer
from .models import StudentModel
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status 

class StudentViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = StudentModel.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        queryset = StudentModel.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        # queryset = StudentModel.objects.all()
        # student = status.get_object_or_404(queryset, pk=pk)
        StudentModel.objects.get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self,request,pk=None):
        # queryset = StudentModel.objects.all()
        student_obj = StudentModel.objects.get(id=pk)
        serializer_obj = StudentSerializer(student_obj)
        return Response(serializer_obj.data)
        




# class StudentViewset(viewsets.ModelViewSet):
#     queryset = StudentModel.objects.all()
#     serializer_class = StudentSerializer
