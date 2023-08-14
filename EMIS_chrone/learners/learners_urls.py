from django.urls import path

from .views import learners_view

urlpatterns = [
    path('', learners_view, name="learners")
]