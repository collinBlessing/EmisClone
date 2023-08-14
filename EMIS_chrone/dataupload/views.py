import random
from django.shortcuts import render
from .models import Learners
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from dashboard.views import fetch_data

# Create your views here.


@login_required
def emisdataupload(request):
    return render(request, "emisdataupload.html", fetch_data(request))


# Generate student lin number
def generate_lin_number(initial):
    lin_number = initial
    for _ in range(9):
        lin_number += str(random.randint(0, 9))
    return lin_number


def is_lin_unique(lin):
    return not Learners.objects.filter(LIN=lin).exists()


def UploadData(request):
    username_for_login_personel = request.session.get("data_pass_username")
    if request.method == "POST":
        nationality = request.POST["nationality"]
        # pass nationality initial to the auto generate lin function
        nationality_initial = nationality[0]
        # generate and check for lin uniqueness
        LIN = generate_lin_number(nationality_initial)
        while not is_lin_unique(LIN):
            LIN = generate_lin_number(nationality_initial)

        firstName = request.POST["firstName"]
        sirname = request.POST["sirname"]
        otherNames = request.POST["otherNames"]
        dateOfBirth = request.POST["dateOfBirth"]
        gender = request.POST["gender"]
        isOrphan = request.POST["isOrphan"]
        districtOfBirth = request.POST["districtOfBirth"]
        is_refugee = request.POST["refugee"]
        photo = request.FILES.get("learner_photo", None)

        # get user instance
        try:
            user_instance = get_user_model().objects.get(
                email=username_for_login_personel
            )

            new_student = Learners(
                user=user_instance,
                LIN=LIN,
                firstName=firstName,
                sirname=sirname,
                otherNames=otherNames,
                dateOfBirth=dateOfBirth,
                gender=gender,
                isOrphan=isOrphan,
                districtOfBirth=districtOfBirth,
                is_refugee=is_refugee,
                nationality=nationality,
                photo=photo,
            )
            # save student
            new_student.save()
            # pass message
            messages.success(request, "Learner added successfully")
            return render(request, "emisdataupload.html")
        except get_user_model().DoesNotExist:
            messages.error(request, "could not find user")

    else:
        return render(request, "emisdataupload.html")
