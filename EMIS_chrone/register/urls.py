from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('registerUser', views.register_user_view, name='registerUser'),

]
