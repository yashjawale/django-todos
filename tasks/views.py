from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import forms
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home.html')


def loginview(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("tasks:tasks")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("tasks:tasks")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def taskdetails(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'taskdetails.html', {'task': task})


@login_required(login_url="/login/")
def tasks(request):
    if request.method == "POST":
        form = forms.CreateTask(request.POST)
        if form.is_valid():
            newtask = form.save(commit=False)
            newtask.author = request.user
            newtask.save()
            return redirect("tasks:tasks")
    else:
        form = forms.CreateTask()
    pending_tasks = Task.objects.filter(author=request.user, completed=False).order_by('-deadline')
    completed_tasks = Task.objects.filter(author=request.user, completed=True).order_by('-id')
    return render(request, 'tasks.html',
                  {'pending_tasks': pending_tasks, 'completed_tasks': completed_tasks, 'form': form})


def logoutview(request):
    if request.method == "POST":
        logout(request)
        return redirect('tasks:login')
