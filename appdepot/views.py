from django.shortcuts import render

# Create your views here.
def appdepot(request):
    context = {
    }
    return render(request, 'appdepot/appdepot.html', context)