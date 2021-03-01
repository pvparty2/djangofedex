from django.shortcuts import render

# Create your views here.
def ship(request):
    return render(request, 'fedexapp/ship.html')
