from django.shortcuts import render
from dataupload.models import learners

# Create your views here.


def dashboard(request):
    learnerFetch = learners.objects.all()
    learnerCount = learners.objects.all().count()
    learner_maleCount = learners.objects.filter(gender="male").count()
    learner_femaleCount = learners.objects.filter(gender="female").count()

    context = {
        "learnerFetch": learnerFetch,
        "learnerCount": learnerCount,
        "learner_maleCount": learner_maleCount,
        "learner_femaleCount": learner_femaleCount,
    }
    return render(request, "dashboard.html", context)
