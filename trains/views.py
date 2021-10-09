from django.shortcuts import render
from .models import train
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView
)


def trains(request):
    context = {
        'trains': train.objects.all()
    }
    return render(request, 'trains/trains.html', context)


class trainListView(ListView):
    model = train
    context_object_name = 'trains'
    template_name = 'trains/trains.html'


class trainUpdateView(UpdateView):
    model = train
    fields = ['tid', 'location', 'status', 'remarks']
