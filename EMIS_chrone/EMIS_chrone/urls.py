
from django.contrib import admin
from django.urls import path, include
import login.urls
import register.urls
import dashboard.urls
import dataupload.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(login.urls)),
    path('register/', include(register.urls)),
    path('dashboard/', include(dashboard.urls)),
    path('emisdataupload/', include(dataupload.urls)),
]
