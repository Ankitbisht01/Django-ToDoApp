from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task



# Create your views here.

def addtask(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    #return HttpResponse('testing add task button')
    return redirect('home')

