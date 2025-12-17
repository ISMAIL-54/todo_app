from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks}) 

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        if title:
            Task.objects.create(title=title, description=description, deadline=deadline if deadline else None)
    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.title = request.POST.get("title", "").strip()
        task.description = request.POST.get("description", "").strip()
        if request.POST.get("deadline", "").strip():
            task.deadline = request.POST.get("deadline")
        task.save()
    return redirect("task_list") 

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
