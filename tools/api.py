from copy import Error
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import ToolSerializer, AddNewToolSerializer
from .models import Tool
from accounts.models import MyUser
import json

# POST NewTool
class NewToolApi(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]

    serializer_class = AddNewToolSerializer

    
    def post(self, request, fromat=None):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print('Data')
            print(serializer.data)
            newTool = Tool(
                name = serializer.data.get('name'),
                github_link = serializer.data.get('github_link'),
                rate=0,
                number_of_votes=0,
                user= None if not serializer.data.get('user') else serializer.data.get('user')
            )
            newTool.save()
            return Response(AddNewToolSerializer(newTool).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

# GET all Tools
class GetToolsApi(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ToolSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Tool.objects.all()
        # query = self.request.GET.getlist('')
        # print(self.request)
        # print(queryset)
        # if query:
        #     queryset = queryset.filter(
        #         Q(name__icontains=query) |
        #         Q(description__icontains=query)
        #     ).distinct()

        return queryset