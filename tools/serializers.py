from .models import Tool
from django.contrib.auth import authenticate
from rest_framework import serializers

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ('id','name', 'github_link', 'rate', 'number_of_votes', 'user')

class AddNewToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ('name','github_link', 'user')
        
