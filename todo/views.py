from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Task



# Create your views here.

def addtask(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    #return HttpResponse('testing add task button')
    return redirect('home')

def mark_as_done(requst, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(requst, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')