from django.shortcuts import render

def home(request):
	return render(request, 'home/index.html', )

def trading(request):
	return render(request, 'home/trading.html')
# Create your views here.
