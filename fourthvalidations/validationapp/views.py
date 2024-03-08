from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json.decoder import JSONDecodeError


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        print('json_data', json_data)
        stream = io.BytesIO(json_data)
        print("io.BytesIO(json_data)", stream)
        try:
            python_data = JSONParser().parse(stream)
            print("parsed data", python_data)
            serializer_obj = StudentSerializer(data=python_data)
            if serializer_obj.is_valid():
                serializer_obj.save()
                res = {'msg': 'DATA INSERTED SUCCESSFULLY'}
                print("OK")
                # json_data = JSONRenderer().render(res)
                # return HttpResponse(json_data, content_type='application/json')
                return JsonResponse(data = res)
            else:
                print(serializer_obj.errors)
                json_data = JSONRenderer().render(serializer_obj.errors)
                return HttpResponse(json_data, content_type='application/json')
        except JSONDecodeError as e:
            error_msg = {'error': 'Invalid JSON data: ' + str(e)}
            json_data = JSONRenderer().render(error_msg)
            return HttpResponse(json_data, content_type='application/json')
    else:
        return HttpResponse("Only POST method allowed", status=405)
        

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
        # json_data = JSONRenderer().render(serializer_obj.data)
        # return HttpResponse(json_data,content_type ='application/json')
    
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
        json_data = JSONRenderer().render(serializer_errors)
        return HttpResponse(json_data,content_type ='application/json')