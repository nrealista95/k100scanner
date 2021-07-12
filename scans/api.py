from copy import Error
from django.core.files.base import File
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from .serializers import ScanSerializer, ScanResultsSerializer, UpdateResultsStatusSerializer
from .models import Scan
import json
import os


# POST NewScan
class NewScanApi(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = ScanSerializer

    
    def post(self, request, fromat=None):
        # BIG TODO check if the current apk was already scaned
        if self.request.method == 'POST':
            tools_selected = self.request.data['data']
            apk_file= self.request.FILES['apk_file']
            fs = FileSystemStorage()
            fs.save(apk_file.name,apk_file)
            # user_id=self.request.user
            # tools_selected = serializer.data.get('tools_selected')
            # print(tools_selected)
            # apk_file = serializer.data.get('apk_file')

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

# GET results of a scan 
class ScanResultsApi(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = ScanResultsSerializer

    def get_queryset(self, *args, **kwargs):
        if self.request.method == 'GET':
            query = self.request.GET.get('scan_id','')
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

    # PUT Update "status" of results        
    def put(self, *args, **kwargs):
        if self.request.method == 'PUT':
            serializer = self.serializer_class(data=self.request.data)
            if serializer.is_valid():
                query = self.request.GET.get('scan_id','')
                queryset = Scan.objects.filter(user_id=self.request.user.id, id=query).update(results=serializer.data.get('results'))
                return Response({'Update Success'}, status=status.HTTP_200_OK)
            return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
# PUT Update "status" of results
class UpdateResultsStatusAPI(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UpdateResultsStatusSerializer

    def put(self, *args, **kwargs):
        print('I am here')
        if self.request.method == 'PUT':
            serializer = self.serializer_class(data=self.request.data)
            query = self.request.GET.get('scan_id','')
            body_unicode = self.request.body.decode('utf-8')
            body = json.loads(body_unicode)
            results_from_request = body['content']
            queryset = Scan.objects.filter(user_id=self.request.user.id, id=query).update(results=results_from_request)