from django.shortcuts import render
from django.shortcuts import render_to_response


# Create your views here.

def HomePage(request):
    return render_to_response('Homepage.html')
