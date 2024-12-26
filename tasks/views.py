from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def taskdetails(request, task_id):
    return render(request, 'taskdetails.html', {'task_id': task_id})

def tasks(request):
    return render(request, 'tasks.html')