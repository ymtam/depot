from django.shortcuts import render
<<<<<<< HEAD
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
=======

# Create your views here.
>>>>>>> 3bd82cf312519771f4dce2d198a701070b0e52a6
