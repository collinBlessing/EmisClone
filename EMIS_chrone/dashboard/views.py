from django.shortcuts import render
from dataupload.models import learners

# Create your views here.

def dashboard(request):
    pic = learners.objects.all()
    return render(request, 'dashboard.html',{'i':pic})