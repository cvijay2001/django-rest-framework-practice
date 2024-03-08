from django.shortcuts import render
from .deserializers import StudentSerializer
from .models import Student
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        print('json_data',json_data)
        stream = io.BytesIO(json_data)
        print("io.BytesIO(json_data ", stream)
        python_data = JSONParser().parse(stream)
        print("pasrsed data",python_data)
        serializer_obj = StudentSerializer(data = python_data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            res = {'msg': 'DATA INSERTED SUCCESSFULLY'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type ='application/json') 
            return JsonResponse(res,content_type ='application/json') 
        else:
            print(serializer_obj.errors)
            json_data = JSONRenderer().render(serializer_obj.errors)
            return HttpResponse(json_data,content_type ='application/json') 


def get_student(request):
    if request.method == 'GET':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id:
            stu = Student.objects.get(id=id)
            serializer_obj = StudentSerializer(stu)
            return JsonResponse(data = serializer_obj.data)
        stu = Student.objects.all()
        serializer_obj = StudentSerializer(stu,many=True)
        return JsonResponse(data = serializer_obj.data)    
