from django.db import models
from django.contrib.auth import get_user_model


# create class
class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(
        max_length=20,
        choices=[("non_staff", "Non-Staff"), ("teaching_staff", "Teaching Staff")],
    )
    gender = models.CharField(max_length=6)
    department = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="staff_pictures/", blank=True, null=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, default="", null=True
    )

    def __str__(self):
        return self.name
