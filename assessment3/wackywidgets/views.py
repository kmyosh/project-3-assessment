
from django.http import HttpResponse
from django.contrib import admin
from django.shortcuts import render
# Create your views here.

def index(request):
    return HttpResponse("Hello")

def home(request):
    return render(request,'home.html')