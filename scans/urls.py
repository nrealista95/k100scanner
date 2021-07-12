from django.urls import path, include
from .api import NewScanApi, ScanListApi, ScanResultsApi, UpdateResultsStatusAPI
# from knox import views as knox_views

urlpatterns = [
    # path('scan', include('knox.urls')),
    path('scans', ScanListApi.as_view()),
    path('newscan', NewScanApi.as_view()),
    path('scans/results/', ScanResultsApi.as_view())
]
