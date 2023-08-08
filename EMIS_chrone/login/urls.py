from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('registerUser', views.login, name="registerUser"),
]
