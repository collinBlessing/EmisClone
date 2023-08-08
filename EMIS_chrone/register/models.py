from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.EmailField(max_length=254)
    