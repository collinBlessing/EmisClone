from django.db import models


# Create your models here.
class Users(models.Model):
    userEmail = models.EmailField(max_length=254, null=False, blank=False)
    firstName = models.TextField(max_length=254, null=False, blank=False)
    lastname = models.TextField(max_length=254, null=False, blank=False)
    userPassword = models.TextField(max_length=50, null=False, blank=False)
    institutionType = models.TextField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.userEmail
