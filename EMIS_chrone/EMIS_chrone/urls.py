from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import dashboard.urls
import dataupload.urls
from signin_signup import signin_urls
from signin_signup import signup_urls
from staff_registration import staff_regurls
from learners import learners_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(signin_urls)),
    path("register/", include(signup_urls)),
    path("dashboard/", include(dashboard.urls)),
    path("emisdataupload/", include(dataupload.urls)),
    path("staff_reg/", include(staff_regurls)),
    path("logout/", include(signin_urls)),
    path("learners/", include(learners_urls)),
    path("license/", include(learners_urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
