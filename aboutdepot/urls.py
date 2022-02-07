from django.urls import path

from .views import aboutdepot

urlpatterns = [
    path('',aboutdepot,name="aboutdepot"),
]