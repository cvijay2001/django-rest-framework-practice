from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)  # Set required=False
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    # def validate_roll(self,value):
    #     if value > 300:
    #         raise serializers.ValidationError('Roll should not be greater than 300')
    #     return value
   
    def validate(self,data):
        print(data.get("roll"))
        # data is dictionary so now u can access all the values from data as data.get()
        return data
