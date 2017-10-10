from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, World. Youre at the polls index.")
# Create your views here.
