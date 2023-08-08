import random
from django.shortcuts import render
from .models import Learners
from django.contrib import messages

# Create your views here.


def emisdataupload(request):
    return render(request, "emisdataupload.html")


# Generate student lin number
def generate_lin_number():
    lin_number = "U"
    for _ in range(9):
        lin_number += str(random.randint(0, 9))
    return lin_number


# if __name__ == "__main__":
#     lin_number = generate_lin_number()
#     print("Generated LIN number:", lin_number)


def UploadData(request):
    if request.method == "POST":
        LIN = generate_lin_number()
        # check_for_NINS = learners.objects.all()
        # for everyNin in check_for_NINS:
        #     if everyNin == LIN:
        #         LIN = generate_lin_number()
        #     else:
        #         LIN = LIN

        firstName = request.POST["firstName"]
        sirname = request.POST["sirname"]
        otherNames = request.POST["otherNames"]
        dateOfBirth = request.POST["dateOfBirth"]
        gender = request.POST["gender"]
        isOrphan = request.POST["isOrphan"]
        districtOfBirth = request.POST["districtOfBirth"]
        is_refugee = request.POST["refugee"]
        nationality = request.POST["nationality"]
        photo = request.FILES.get("learner_photo", None)

        new_student = Learners(
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
        new_student.save()
        messages.success(request, "Learner added successfully")
        return render(request, "emisdataupload.html")
    else:
        messages.error(request, "An Error occured while submitting data")
        return render(request, "emisdataupload.html")
