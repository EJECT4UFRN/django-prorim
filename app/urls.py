from django.conf.urls import url, include
from django.conf import settings

from app.views import *

urlpatterns = [
	url(r'^',
        IndexView.as_view(),
        name='index'),
]
