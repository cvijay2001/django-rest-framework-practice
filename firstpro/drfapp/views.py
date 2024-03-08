from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse, JsonResponse


def home(request, pk=None):
    if pk is not None:
        stu = Student.objects.get(id=pk)
        serializer_obj = StudentSerializer(stu)
    else:
        stu = Student.objects.all()
        serializer_obj = StudentSerializer(stu, many=True)
        
    # json_data = JSONRenderer().render(serializer_obj.data)
    # return HttpResponse(json_data, content_type='application/json')
        
    return JsonResponse(serializer_obj.data,safe=False)
