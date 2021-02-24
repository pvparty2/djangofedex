from django.shortcuts import render

# Create your views here.
def fedex_ship(request):
    return render(request, 'fedexapp/fedex_ship.html')
