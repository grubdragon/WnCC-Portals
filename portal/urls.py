from django.conf.urls import url
from django.conf.urls import url,include
import views

urlpatterns = [
    url(r'^login/', views.index),
    url(r'^accounts/profile/',views.profile,name='profile')
    
]
