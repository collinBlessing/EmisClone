from django.shortcuts import render
from dataupload.models import Learners
from django.db.models import Q


# Create your views here.
def learners_view(request):
    user_id = request.user.id
    learnerFetch = Learners.objects.filter(user=user_id)
    learnes_with_age = []
    context = {
        "learnerFetch": learnerFetch,
    }

    return render(request, "learners.html", context)


# license view
def license_view(request):
    date = request.user.date_joined
    school_name = request.user.Userschoolname
    context = {"reg_date": date, "school_name": school_name, "academic_year": "2023"}
    return render(request, "license_letter.html", context)


# calculate age
# def calc_age(dateOfBirth):
#     today = date.today()
#     age = (
#         today.year
#         - dateOfBirth.year
#         - ((today.month, today.day) < (dateOfBirth.month, dateOfBirth.day))
#     )
#     return age
