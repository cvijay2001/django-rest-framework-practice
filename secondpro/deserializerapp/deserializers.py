from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)  # Set required=False
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

    def create(self, validate_data):
        print(validate_data)
        return Student.objects.create(**validate_data)