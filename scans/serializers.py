from .models import Scan, NewScan
from django.contrib.auth import authenticate
from rest_framework import serializers

class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan
        fields = ('app_name', 'app_icon', 'risk_score', 'md5', 'time')

class NewScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewScan
        fields = ('tool_selected', 'user', 'apk_file')