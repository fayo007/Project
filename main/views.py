from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def about(request):
    email = request.GET.get('email')
    print(email)
    return render(request, 'about.html')

def contact(request):
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    email = request.GET.get('email')
    message = request.GET.get('message')
    subject = request.GET.get('subject')
    print(name)
    print(phone)
    print(email)
    print(message)
    print(subject)
    return render(request, 'contact.html')

def index(request):
    return render(request,'index.html')

def price(request):
    return render(request,'price.html')

def projects(request):
    return render(request,'projects.html')

def services(request):
    email = request.GET.get('email')
    print(email)
    return render(request, 'service.html')

def sidebar_right(request):
    return render(request,'sidebar-right.html')

