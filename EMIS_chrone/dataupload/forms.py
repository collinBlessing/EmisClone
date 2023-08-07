# forms.py
from django import forms

class LearnerForm(forms.Form):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    NIN_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    REFUGEE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    photo = forms.ImageField()
    firstName = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    otherNames = forms.CharField(max_length=100, required=False)
    dateOfBirth = forms.DateField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    isOrphan = forms.ChoiceField(choices=YES_NO_CHOICES, widget=forms.RadioSelect)
    districtOfBirth = forms.CharField(max_length=100)
    has_NIN = forms.ChoiceField(choices=NIN_CHOICES, widget=forms.RadioSelect)
    is_refugee = forms.ChoiceField(choices=REFUGEE_CHOICES, widget=forms.RadioSelect)
    nationality = forms.CharField(max_length=100)
