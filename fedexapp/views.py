from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactForm

# Create your views here.
def ship(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect('/shipped/')
    # if a GET (or any other method), create a blank form
    else:
        form = ContactForm()

    return render(request, 'fedexapp/ship.html', {'form': form})

def shipped(request):
    return render(request, 'fedexapp/shipped.html')
