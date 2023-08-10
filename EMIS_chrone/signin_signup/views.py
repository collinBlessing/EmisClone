from django.shortcuts import render


# Create your views here.
# user signin view
def sign_in_view(request):
    return render(request, "login.html")


# user signup view
def sign_up_view(request):
    return render(request, "register.html")


# register user
def register_user_view(request):
    pass
