
from django.conf import settings
from django.conf.urls.static import static
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
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
