from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test_function(request):
    return HttpResponse("<h1>Hello World<h1>")

def home_view(request):
    return render(request, 'home.html', context={})