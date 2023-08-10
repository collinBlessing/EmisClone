from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import login.urls
import dashboard.urls
import dataupload.urls

from login import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(login.urls)),
    path("dashboard/", include(dashboard.urls)),
    path("emisdataupload/", include(dataupload.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
