from django.urls import path

from .views import *

app_name = "files"

urlpatterns = [
    path('file_upload/', file_upload, name='file_upload'),
    path('get/file_upload/', get_file_upload, name='get_file_upload'),
    path('get/files/', files_api, name='files_api'),

]
