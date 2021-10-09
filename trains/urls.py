from django.urls import path
from trains.views import trainListView, trainUpdateView

urlpatterns = [
    path('', trainListView.as_view(), name="trains-list"),
    path('<str:pk>/', trainUpdateView.as_view(), name="trains-update"),
]
