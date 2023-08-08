import random
from django.shortcuts import render
from .models import Learners
from django.contrib import messages

# Create your views here.


def emisdataupload(request):
    return render(request, "emisdataupload.html")


# Generate student lin number
def generate_lin_number(initial):
    lin_number = initial
    for _ in range(9):
        lin_number += str(random.randint(0, 9))
    return lin_number


# if __name__ == "__main__":
#     lin_number = generate_lin_number()
#     print("Generated LIN number:", lin_number)


def UploadData(request):
    if request.method == "POST":
        nationality = request.POST["nationality"]
        # pass nationality initial to the auto generate lin function
        nationality_initial = nationality[0]
        LIN = generate_lin_number(nationality_initial)
        # check_for_NINS = learners.objects.all()
        for everyNin in Learners.objects.all():
            while LIN == everyNin:
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
