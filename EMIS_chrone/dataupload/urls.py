
from django.urls import path
from . import views

urlpatterns = [
    path("", views.emisdataupload),
    path("upload/", views.UploadData, name="upload_data"),
]
