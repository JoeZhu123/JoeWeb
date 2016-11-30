from django.shortcuts import render
# -*-coding:utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response


def InternetIndex1(request):
	return render_to_response('InternetIndex1.html')

