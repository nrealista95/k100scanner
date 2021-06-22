from copy import Error
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.core import serializers
from knox.models import AuthToken
from .serializers import NewScanSerializer, ScanSerializer, ScanResultsSerializer
from .models import Scan, NewScan
from accounts.models import MyUser
import json


# POST NewScan
class NewScanApi(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = NewScanSerializer

    
    def post(self, request, fromat=None):
        # BIG TODO check if the current apk was already scaned
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # user_id=self.request.user
            user_id = serializer.data.get('tool_selected')
            tool_selected = serializer.data.get('tool_selected')
            apk_file = serializer.data.get('apk_file')

            # TODO with the data provided start the scan
            #
            # Call the appsentinel scanner here!
            #
            # END OF SCAN

            # test = Scan.objects.raw("SELECT 2 id, results -> 'results' ->> 'M1' FROM scans_scan")
            # json_output = serializers.serialize('json', test)
            # print(json_output)

            with open("/home/narfa/Documents/K100infoSec/Projects/k100scanner/scans/results_sample.json") as json_file:
                results_data = json.load(json_file)
            
            newscan = Scan(app_name='qq coisa',
            user=self.request.user,
            risk_score=10,
            md5=4,
            time='14:30:59',
            results=results_data)
            print('------------------------')
            print(newscan.user)
            newscan.save()
            return Response(ScanSerializer(newscan).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

# GET all user scans
class ScanListApi(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ScanSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Scan.objects.filter(user_id=self.request.user.id)
        query = self.request.GET.getlist('')
        print(self.request)
        print(queryset)
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            ).distinct()

        return queryset

class ScanResultsApi(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = ScanResultsSerializer

    def get_queryset(self, *args, **kwargs):
        if self.request.method == 'GET':
            query = self.request.GET.get('scan_id','')
            print(kwargs)
            print(query)
            queryset = ''
            if query == '':
                print(Error)
            else:
                queryset = Scan.objects.filter(user_id=self.request.user.id, id=query).distinct()
            print('Query set:')
            print(queryset)
            # if query:
            #     queryset = queryset.filter(
            #         Q(name__icontains=query) |
            #         Q(description__icontains=query)
            #     ).distinct()

            return queryset
