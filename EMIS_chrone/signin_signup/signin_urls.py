from django.urls import path
from .views import sign_in_view, sign_in_user, logout_view

urlpatterns = [
    path("", sign_in_view, name="login"),
    path("auth", sign_in_user, name="auth"),
    path("logout", logout_view, name="logout"),
]
