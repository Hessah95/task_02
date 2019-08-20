from django.shortcuts import render

# Create your views here.

def vw (request) :

	context = {
	"msg" : "Hello world!",
	}

	return render (request, 'test.html', context)