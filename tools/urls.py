from django.urls import path
from .api import NewToolApi, GetToolsApi

urlpatterns = [
    path('admin/newtool', NewToolApi.as_view()),
    path('tools', GetToolsApi.as_view())
]