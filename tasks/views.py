from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import forms

def index(request):
    return render(request, 'home.html')

def login(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    form  = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def taskdetails(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'taskdetails.html', {'task': task})

def tasks(request):
    pending_tasks = Task.objects.filter(completed=False).order_by('-deadline')
    completed_tasks = Task.objects.filter(completed=False).order_by('-id')
    form = forms.CreateTask()
    return render(request, 'tasks.html', {'pending_tasks': pending_tasks, 'completed_tasks': completed_tasks, 'form': form})