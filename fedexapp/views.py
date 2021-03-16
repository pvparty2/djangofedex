from django.shortcuts import render, redirect

from .forms import ShipmentForm, UploadFileForm
from .banners.shipper import shipper
from .banners.my_function import handle_uploaded_file

# Create your views here.
def ship(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ShipmentForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect('/shipped/')
    # if a GET (or any other method), create a blank form
    else:
        form = ShipmentForm(initial=shipper)

    return render(request, 'fedexapp/ship.html', {'form': form})

def shipped(request):
    return render(request, 'fedexapp/shipped.html')

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.POST)
            return redirect('fedexapp:shipped')
    else:
        form = UploadFileForm()
    return render(request, 'fedexapp/upload.html', {'form': form})