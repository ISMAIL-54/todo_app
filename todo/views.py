from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Adjust bootstrap
#def gui(request):
#   return render(request, 'tasks/task_list.html')

def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        if title:
            Task.objects.create(title=title, description=description, deadline=deadline if deadline else None)
        return redirect('task_list')

    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks}) 

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')