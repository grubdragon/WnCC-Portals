from django.conf.urls import url
from portal.views import *

urlpatterns = [
    url(r'student/(?P<pk>[0-9]{1})$', register),
]
