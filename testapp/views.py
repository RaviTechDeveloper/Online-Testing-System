from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greeting(request):
    s="<h1>Hello ravi you are good boy</h1>"
    return HttpResponse(s)
def about(request):
    s="<h1>About Page</h1>" 
    return HttpResponse(s)   
def contacts(request):
    s="<h1>Contact Page</h1>"
    return HttpResponse(s)