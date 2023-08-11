from django.shortcuts import render
from dataupload.models import Learners
from django.db.models import Q

# Create your views here.


def dashboard(request):
    # fetch user email from the session
    username_for_login_personel = request.session.get("data_pass_username")
    # initialise multiple filter conditions

    # male conditioning
    males_condition_one = Q(gender="male")
    males_condition_two = Q(user=username_for_login_personel)

    # female conditioning
    females_condition_one = Q(gender="female")
    females_condition_two = Q(user=username_for_login_personel)

    # initialise learnercount, learnermale_count and learner_female_count variable

    # initialise total  learners count
    learnerCount = Learners.objects.filter(user=username_for_login_personel).count()

    # conditions for filtering out males and females based in the previously defined conditioning above
    # male conditioning
    learner_maleCount = Learners.objects.filter(
        males_condition_one & males_condition_two
    ).count()

    # female cinditioning
    learner_femaleCount = Learners.objects.filter(
        females_condition_one & females_condition_two
    ).count()

    # pass in the context
    context = {
        "learnerCount": learnerCount,
        "learner_maleCount": learner_maleCount,
        "learner_femaleCount": learner_femaleCount,
        "username": username_for_login_personel,
    }
    return render(request, "dashboard.html", context)
