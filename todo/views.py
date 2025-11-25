from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')

    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks}) 

