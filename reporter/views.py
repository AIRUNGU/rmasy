from django.shortcuts import render

# Create your views here.

def HomeP(request):
	return render(request,'welcome.html',{})