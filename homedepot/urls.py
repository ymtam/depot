from django.urls import path

from .views import homedepot

urlpatterns = [
    path('',homedepot,name="homedepot"),
]