from django.shortcuts import render
from django.http import HttpResponse
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
def home(request):
	return render(request,'neha.html')

def gallery(request):
	
	path=str(BASE_DIR)+"/static/neha_img/"
	images=os.listdir(path)
	return render(request,'gallery.html',{'object':images})
	


