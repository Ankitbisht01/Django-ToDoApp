from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False)
    completedtasks = Task.objects.filter(is_completed = True)
    data = {
        'tasks': tasks,
        'completedtasks' : completedtasks,
    }
    completedtasks = Task.objects.filter(is_completed = True)

    return render(request, 'index.html',data)