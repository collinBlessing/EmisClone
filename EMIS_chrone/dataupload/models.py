from django.db import models


# Create your models here.
class Learners(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
    ]
    YES_NO_CHOICES = [
        ("yes", "Yes"),
        ("no", "No"),
    ]

    NIN_CHOICES = [
        ("yes", "Yes"),
        ("no", "No"),
    ]

    REFUGEE_CHOICES = [
        ("yes", "Yes"),
        ("no", "No"),
    ]
    LIN = models.CharField(max_length=11, null=True, auto_created=True)
    firstName = models.CharField(max_length=100)
    sirname = models.CharField(max_length=100)
    otherNames = models.CharField(max_length=100, blank=True)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    isOrphan = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    districtOfBirth = models.CharField(max_length=100)
    # refugee model
    is_refugee = models.CharField(max_length=3, choices=REFUGEE_CHOICES)
    # nationality model
    nationality = models.CharField(max_length=100)
    # photo model
    photo = models.ImageField(upload_to="learners/", blank=True)

    def __str__(self):
        return self.firstName
