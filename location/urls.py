from django.urls import path
from .views import locationUpdateView,update_location,location

urlpatterns = [
    path('',location,name="location"),
    path('test/',update_location,name="location-test"),
    path('<str:pk>/',locationUpdateView.as_view(),name="location-update"),
]