from django.shortcuts import render
from .models import models
from .serializers import StudentSerializer
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
import io
from .models import Student
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import io
from .serializers import StudentSerializer

# @csrf_exempt
# def student_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer_obj = StudentSerializer(data=python_data)
#         if serializer_obj.is_valid():
#             serializer_obj.save()
#             res = {'msg': 'Student CREATED Successfully'}
#             return JsonResponse(data=res)
#         else:
#             res = {'msg': 'Student Not Created-->' + str(serializer_obj.errors)}
#             return JsonResponse(data=res)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            
            serializer_obj = StudentSerializer(data=python_data)
            
            if serializer_obj.is_valid():
                serializer_obj.save()
                res = {'msg': 'Student CREATED Successfully'}
                return JsonResponse(data=res)
            else:
                res = {'msg': 'Student Not Created', 'errors': serializer_obj.errors}
                return JsonResponse(data=res, status=400)  # Bad Request
        except Exception as e:
            res = {'msg': 'Internal Server Error', 'error_details': str(e)}
            return JsonResponse(data=res, status=500)  # Internal Server Error
    else:
        res = {'msg': 'Invalid Request Method'}
        return JsonResponse(data=res, status=405)  # Method Not Allowed


    

def get_student(request):
    print('GETSTUDENT Funcion executed')
    if request.method == 'GET':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id:
            stu = Student.objects.get(id=id)
            serializer_obj = StudentSerializer(stu)
            print('Serialzer onnly one  data', serializer_obj.data)

            return JsonResponse(data = serializer_obj.data)
            # json_data = JSONRenderer().render(serializer_obj.data)
            # return HttpResponse(json_data,content_type ='application/json') 

        stu = Student.objects.all()
        serializer_obj = StudentSerializer(stu,many=True)
        return JsonResponse(data = serializer_obj.data,safe=False)
    

@csrf_exempt
def update_student(request):
    print("update_student function execuded")
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        stu_id = python_data.get('id')
        stu = Student.objects.get(id=stu_id)
        print('student: obj',stu)
        serializer_obj= StudentSerializer(instance=stu,data=python_data,partial=True)
        print(serializer_obj)
        print('is valid checking')
        if serializer_obj.is_valid():
            serializer_obj.save()
            res = {'msg': "DATA UPADTED SUCCESSFULLY"}
            return JsonResponse(data=res)
        serializer_errors  = serializer_obj.errors
        return JsonResponse(serializer_errors)
    

@csrf_exempt
def student_delete(request, pk):
    if request.method == 'DELETE':
        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            return JsonResponse({'msg': 'Student deleted successfully'})
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
