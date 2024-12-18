from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'website/index.html')
  # return HttpResponse("Hello, world. You are at chai aur Django Home Page")

def about(request):
    return HttpResponse("Hello, world. You are at chai aur Django About Page")

def contact(request):
    return HttpResponse("Hello, world. You are at chai aur Django Contact Page")