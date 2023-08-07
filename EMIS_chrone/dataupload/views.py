import random
from django.shortcuts import render
from .models import learners

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

        new_student = learners(
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
        print("done")
        return render(request, "emisdataupload.html", {"result_message": "success"})
    else:
        return render(request, "emisdataupload.html", {"result_message": "error"})
