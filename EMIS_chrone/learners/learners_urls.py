from django.urls import path

from .views import learners_view,license_view

urlpatterns = [
    path("", learners_view, name="learners"),
    path("license/", license_view, name="license"),
]
