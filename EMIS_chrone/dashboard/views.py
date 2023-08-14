from django.shortcuts import render
from dataupload.models import Learners
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from staff_registration.models import Staff

# Create your views here.


@login_required
def dashboard(request):
    return render(request, "dashboard.html", fetch_data(request))


def fetch_data(request):
    username_for_login_personel = request.session.get("data_pass_username")
    # get id
    user_id = request.user.id
    user_firstname = request.user.first_name
    user_lastname = request.user.last_name

    # initialise multiple filter conditions

    # male conditioning
    males_condition = Q(gender="male") & Q(user=user_id)

    # female conditioning
    females_condition = Q(gender="female") & Q(user=user_id)

    # select for staff and non staff
    Staff_condition = Q(role="teaching_staff") & Q(user=user_id)
    NonStaff_condition = Q(role="non_staff") & Q(user=user_id)

    # male conditioning
    Staff_males_condition = (
        Q(gender="male") & Q(user=user_id) & Q(role="teaching_staff")
    )

    # female conditioning
    Staff_females_condition = (
        Q(gender="female") & Q(user=user_id) & Q(role="teaching_staff")
    )
    # male conditioning
    NonStaff_males_condition = Q(gender="male") & Q(user=user_id) & Q(role="non_staff")

    # female conditioning
    NonStaff_females_condition = (
        Q(gender="female") & Q(user=user_id) & Q(role="non_staff")
    )

    # initialise learnercount, learnermale_count and learner_female_count variable
    #  fetch  all learners of the user id
    learnerFetch = Learners.objects.filter(user=user_id)

    # initialise total  learners count
    learnerCount = Learners.objects.filter(user=user_id).count()
    # initialise total  learners count

    StaffCount = Staff.objects.filter(Staff_condition).count()

    NonStaffCount = Staff.objects.filter(NonStaff_condition).count()

    # conditions for filtering out males and females based in the previously defined conditioning above
    # male conditioning
    learner_maleCount = Learners.objects.filter(males_condition).count()
    Staff_maleCount = Staff.objects.filter(Staff_males_condition).count()
    NonStaff_maleCount = Staff.objects.filter(NonStaff_males_condition).count()

    # female cinditioning
    learner_femaleCount = Learners.objects.filter(females_condition).count()
    Staff_femaleCount = Staff.objects.filter(Staff_females_condition).count()
    NonStaff_femaleCount = Staff.objects.filter(NonStaff_females_condition).count()

    # pass in the context
    context = {
        #
        "learnerFetch": learnerFetch,
        "learnerCount": learnerCount,
        "learner_maleCount": learner_maleCount,
        "learner_femaleCount": learner_femaleCount,
        # staff
        "staffCount": StaffCount,
        "staff_maleCount": Staff_maleCount,
        "staff_femaleCount": Staff_femaleCount,
        # non staff
        "Non_staffCount": NonStaffCount,
        "Non_staff_maleCount": NonStaff_maleCount,
        "Non_staff_femaleCount": NonStaff_femaleCount,
        # username
        "user_firstname": user_firstname,
        "user_firstname_init": user_firstname[0],
        "user_lastname": user_lastname,
        "user_lastname_init": user_lastname[0],
    }
    return context
