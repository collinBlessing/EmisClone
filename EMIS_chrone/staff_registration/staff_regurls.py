from django.urls import path
from .views import staff_view, staff_UploadData

urlpatterns = [
    path("", staff_view, name="staff_reg"),
    path("registerstaff", staff_UploadData, name="register_staff"),
]
