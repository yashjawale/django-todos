from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginview, name='login'),
    path('register/', views.register, name='register'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>/', views.taskdetails, name='taskdetails'),
    path('logout/', views.logoutview, name='logout')
]
