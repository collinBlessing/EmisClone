from django.shortcuts import render

# Create your views here.

def emisdataupload(request):
    return render(request, 'emisdataupload.html')