from django.shortcuts import render
from dataupload.models import Learners
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def dashboard(request):
    # fetch user email from the session and get its id
    username_for_login_personel = request.session.get("data_pass_username")
    # get id
    user_id = request.user.id
    print(user_id)

    # initialise multiple filter conditions

    # male conditioning
    males_condition = Q(gender="male") & Q(user=user_id)

    # female conditioning
    females_condition = Q(gender="female") & Q(user=user_id)

    # initialise learnercount, learnermale_count and learner_female_count variable
    #  fetch  all learners of the user id
    learnerFetch = Learners.objects.filter(user=user_id)

    # initialise total  learners count
    learnerCount = Learners.objects.filter(user=user_id).count()

    # conditions for filtering out males and females based in the previously defined conditioning above
    # male conditioning
    learner_maleCount = Learners.objects.filter(males_condition).count()

    # female cinditioning
    learner_femaleCount = Learners.objects.filter(females_condition).count()

    # pass in the context
    context = {
        "learnerFetch": learnerFetch,
        "learnerCount": learnerCount,
        "learner_maleCount": learner_maleCount,
        "learner_femaleCount": learner_femaleCount,
        "username": username_for_login_personel,
    }
    return render(request, "dashboard.html", context)
