from django.urls import path

from .views import *

app_name = "files"

urlpatterns = [
    path('file_upload/', file_upload, name='file_upload'),

]
