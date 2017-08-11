# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('app.urls')),
    url(r'^rest-auth/', include('rest_auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
