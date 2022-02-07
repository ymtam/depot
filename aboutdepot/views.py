from django.shortcuts import render

# Create your views here.
def aboutdepot(request):
    context = {
    }
    return render(request, 'aboutdepot/aboutdepot.html', context)