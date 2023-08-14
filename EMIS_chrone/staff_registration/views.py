from django.shortcuts import render
from .models import Staff
from django.contrib.auth import get_user_model
from django.contrib import messages


# Create your views here.
def staff_view(request):
    return render(request, "staff_reg.html")


# register employee
def staff_UploadData(request):
    username_for_login_personel = request.session.get("data_pass_username")
    if request.method == "POST":
        staff_name = request.POST["name"]
        staff_email = request.POST["email"]
        staff_role = request.POST["role"]
        staff_gender = request.POST["gender"]
        staff_department = request.POST["department"]
        staff_qualification = request.POST["qualification"]
        photo = request.FILES.get("picture", None)

        # get user instance
        try:
            user_instance = get_user_model().objects.get(
                email=username_for_login_personel
            )

            new_staff = Staff(
                user=user_instance,
                name=staff_name,
                email=staff_email,
                role=staff_role,
                gender=staff_gender,
                department=staff_department,
                qualification=staff_qualification,
                picture=photo,
            )
            # save student
            new_staff.save()
            # pass message
            messages.success(request, "Staff member added successfully")
            return render(request, "staff_reg.html")
        except get_user_model().DoesNotExist:
            messages.error(request, "could not find user")

    else:
        return render(request, "staff_reg.html")
