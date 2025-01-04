from rest_framework import serializers
from .models import Employee
import re


class Employee_serializer(serializers.Serializer):
    ID = serializers.CharField()
    Name = serializers.CharField()
    Age = serializers.CharField()

    def validate_emp_id(self,value):
        if re.match('\w[\d]+',value) == None or len(value) >= 8:
            raise serializers.ValidationError('Please enter valid employee id')
        else:
            return value
        
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    def update(self,instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance,key,value)
        instance.save()
        return instance
    
    class meta:
        model = Employee
        field = "__all__"