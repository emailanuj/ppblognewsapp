from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def News(request):
    return HttpResponse('<h1>Hey Test Page From programming planet<h1>')

def Home(request):
    return HttpResponse('<b>This is home page</b>')

def Latest(request):
    return HttpResponse('<b>This is latest news page</b>')