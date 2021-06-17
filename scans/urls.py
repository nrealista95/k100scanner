from django.urls import path, include
from .api import NewScanApi, ScanListApi
# from knox import views as knox_views

urlpatterns = [
    # path('scan', include('knox.urls')),
    path('scans', ScanListApi.as_view()),
    path('newscan', NewScanApi.as_view())
]
