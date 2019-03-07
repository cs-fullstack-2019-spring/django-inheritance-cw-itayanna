from django.shortcuts import render
from .forms import ContactForm
# Create your views here.

def index(request):
    return render(request, 'CodeCrewMockApp/index.html')

def aboutUs(request):
    return render(request, 'CodeCrewMockApp/aboutUs.html')

def gallery(request):
    return render(request, 'CodeCrewMockApp/gallery.html')

def contactUs(request):
    form = ContactForm
    return render(request, 'CodeCrewMockApp/contactUs.html',{'form': form})

def resources(request):

    return render(request, 'CodeCrewMockApp/resources.html', )
