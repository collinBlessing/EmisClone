from django.shortcuts import render, redirect

# from .forms import RegistrationForm
from django.contrib import messages
from .models import School_register
from django.contrib.auth import authenticate, login, hashers, logout


# Create your views here.
# user signin view
def sign_in_view(request):
    return render(request, "login.html")


# user signup view
def sign_up_view(request):
    return render(request, "register.html")


def logout_view(request):
    logout(request)
    return render(request, "login.html")


# register user
def register_user_view(request):
    if request.method == "POST":
        Useremail = request.POST.get("Useremail")
        Userfirstname = request.POST.get("Userfirstname")
        Userlastname = request.POST.get("Userlastname")
        Userpassword = request.POST.get("Userpassword")
        Userschoolname = request.POST.get("Userschoolname")
        institutionType = request.POST.get("institutionType")

        hashed_password = hashers.make_password(Userpassword)
        new_user = School_register(
            username=Useremail,
            email=Useremail,
            password=hashed_password,
            first_name=Userfirstname,
            last_name=Userlastname,
            Userschoolname=Userschoolname,
            institutionType=institutionType,
        )
        new_user.save()
        messages.success(request, "Registered successfully")
        return redirect("/")

    else:
        messages.error(request, "Something went wrong, please try again")
        return render(
            request,
            "register.html",
        )


# signin
def sign_in_user(request):
    if request.method == "POST":
        Useremail = request.POST.get("Useremail")
        Userpassword = request.POST.get("Userpassword")
        user_auth_result = authenticate(
            request, username=Useremail, password=Userpassword
        )

        if user_auth_result:
            login(request, user_auth_result)
            request.session["data_pass_username"] = user_auth_result.get_username()
            return redirect("dashboard_home")
        else:
            messages.error(request, "Invalid login details, check email or password")
            return redirect("login")
    else:
        return redirect("login")
