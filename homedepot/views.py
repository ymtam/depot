from django.shortcuts import render

# Create your views here.
def homedepot(request):
    context = {
    }
    return render(request, 'homedepot/homedepot.html', context)