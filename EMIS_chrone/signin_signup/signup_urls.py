from django.urls import path
from .views import sign_up_view, register_user_view

urlpatterns = [
    path("", sign_up_view, name="register"),
    path("register_user", register_user_view, name="registerUser"),
]
