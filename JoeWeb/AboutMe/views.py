from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

def AboutMeIndex1(request):
    return render_to_response('AboutMeIndex1.html')