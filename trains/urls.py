from django.urls import path
from trains.views import trainListView, trainUpdateView

urlpatterns = [
    path('', trainListView.as_view(), name="trains-trains"),
    path('<str:pk>/', trainUpdateView.as_view(), name="trains-update"),
]
