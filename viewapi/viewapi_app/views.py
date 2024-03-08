from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def get_student(request,id = None):
    if request.method == 'GET':
        if id:
            student_instance = Student.objects.filter(id= id).first()
            if student_instance:
                serializer_obj = StudentSerializer(student_instance)
                return Response(serializer_obj.data,status=200)
            else:
                return Response({'msg':f"NO student Found with this id-->{id}"})
        else:
            student_instances = Student.objects.all()
            if student_instances.exists():
                serializer_obj = StudentSerializer(student_instances,many=True)
                return Response(serializer_obj.data,status=200)
            else:
                return Response({'msg':"NO student Found "})

# @api_view(['POST','GET'])
# def create_student(request):
    if request.method == 'POST':
        serializer_obj = StudentSerializer(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            res = {'message': 'Data Added Successfully'}
            return Response(res, status=201)  # Return 201 Created status
        else:
            res = {'error': f'Data not added --> error as {serializer_obj.errors}'}
            return Response(res, status=400)  # Return 400 Bad Request status
    
    if request.method == 'PUT':
        id = request.data.get('id')
        student_instance = Student.objects.get(id=id)
        serializer_obj = StudentSerializer(instance=student_instance,data=request.data)
        print("before serizerobj")
        if serializer_obj.is_valid():
            serializer_obj.save()
            res = {'message': 'Data Added Successfully'}
            return Response(res, status=201)  # Return 201 Created status
        else:
            res = {'error': f'Data not added --> error as {serializer_obj.errors}'}
            return Response(res, status=400)  # Return 400 Bad Request status
        

    
    if request.method == 'PATCH':
        id = request.data.get('id')
        student_instance = Student.objects.get(id=id)
        print(student_instance)
        serializer_obj = StudentSerializer(instance=student_instance,data=request.data,partial=True)
        if serializer_obj.is_valid():
            serializer_obj.save()
            res = {'message': 'Partially Data Added Successfully'}
            return Response(res, status=201)  # Return 201 Created status
        else:
            res = {'error': f'Data not added --> error as {serializer_obj.errors}'}
            return Response(res, status=400)  # Return 400 Bad Request status
        
    if request.method == 'DELETE':
        if id:
            student_instance = Student.objects.get(id=id)
            if student_instance:
                student_instance.delete()
                res={"msg":"DAta Deleted Successfully"}
                return Response(res,status=200)
            else:
                return Response({'msg':f"NO student Found with this id-->{id}"})

        

             
            

