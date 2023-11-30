from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from django import forms

class ListTasks(serializers.ModelSerializer): # для вывода
    class Meta: 
        model = Task
        fields = ['id','title', 'body']

class CreateUpdateTask(serializers.ModelSerializer): # для обновки или создания
    class Meta:
        model = Task
        fields = ['title','body']
        
class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True,style={'input_type':'password'})
    confirm_password = serializers.CharField(write_only=True,required=True,style={'input_type':'password'})
    
    class Meta:
        model = User
        fields = ('username','password','confirm_password')
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('these passwords are not match')
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user

class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']