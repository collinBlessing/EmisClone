from django.shortcuts import render
from dataupload.models import Learners

# Create your views here.


def dashboard(request):

    learnerFetch = Learners.objects.all()
    learnerCount = Learners.objects.all().count()
    learner_maleCount = Learners.objects.filter(gender="male").count()
    learner_femaleCount = Learners.objects.filter(gender="female").count()

    context = {
        "learnerFetch": learnerFetch,
        "learnerCount": learnerCount,
        "learner_maleCount": learner_maleCount,
        "learner_femaleCount": learner_femaleCount,
    }
    return render(request, "dashboard.html", context)
