from django.shortcuts import render
from trains.models import train
from .forms import LocationForm
from django.http import HttpResponseRedirect
from django.core import serializers
from django.views.generic import(
    UpdateView
)

def location(request):
    json_string =serializers.serialize('json', train.objects.all(),fields=('location','status'))
    print(json_string)
    context={
        'trains':json_string
    }
    return render(request,'location/location.html',context)  

def update_location(request):

    if request.method == 'POST':
        form =LocationForm(request.POST)        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/depot')
    else:
        form =LocationForm()
        
    return render(request,'location/location_test.html',{'form': form})  

class locationUpdateView(UpdateView):
    model = train
    fields = ['tid','location']