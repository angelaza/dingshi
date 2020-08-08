from django.shortcuts import render

# Create your views here.
import requests


def task(request):

    return render(request,'index.html')
