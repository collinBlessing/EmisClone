from django.contrib import admin
from .models import learners, myInstitution, supportingstaff, teachingstaff

# Register your models here.
admin.site.register(learners)
admin.site.register(myInstitution)
admin.site.register(supportingstaff)
admin.site.register(teachingstaff)
