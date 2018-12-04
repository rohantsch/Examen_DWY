from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registrar(request):
    return render(request, 'registrar.html')

def home(request):
    return render(request, 'home.html')