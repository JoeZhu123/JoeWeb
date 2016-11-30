__author__='Joe'
#._*_coding:utf-8_*_
import re
import sys
import random
from django.shortcuts import render#MVC
from django.http import HttpResponse#NOT MVC
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django import forms
from Robot.models import *

reload(sys)
sys.setdefaultencoding('utf8')

# Create your views here.
def RobotIndex1(request):
    return render_to_response('RobotIndex1.html')
    
# Create your views here.    
def RobotIndex2(request):
	return render(request, 'RobotIndex2.html')

def RobotIndex3(request):
	if request.method=="POST":
		#uf=UploadFileForm(request.POST,request.FILES)
		#if uf.is_valid():
		f=request.FILES['file']
		handle_uploaded_file(f)
		combin=(f.name).split('.')[0]
		stocks=[]
		length_lines=0
		check_box_list=[]
		check_box_list = request.POST.getlist("check_box_list")
		for chunk in f.chunks():
			lines=re.split('\n',chunk)
			length_lines=len(lines)
			for line in lines:
				l=line.split(' ')
				if len(l)<3:continue
				stock=Stock()
				stock.ID=l[0]
				stock.Name=l[1].decode('gbk')
				stock.Volume=l[2]
				stocks.append(stock)
				#insert stocks into database
				if len(check_box_list)==1:
					stockdb=DB_Stock(Combin=combin,ID=stock.ID,Name=stock.Name,Volume=stock.Volume)
					stockdb.save()
		print length_lines
		return render_to_response('RobotIndex3.html',locals())
	else:
		uf=UploadFileForm()
	return render_to_response('RobotIndex3.html',locals())



