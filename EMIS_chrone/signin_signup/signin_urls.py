from django.urls import path
from .views import sign_in_view

urlpatterns = [path("", sign_in_view,name="login")]
