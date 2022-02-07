from django.urls import path

from .views import appdepot

urlpatterns = [
    path('',appdepot,name="appdepot"),
]