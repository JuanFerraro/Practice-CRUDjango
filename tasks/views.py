from django.shortcuts import render, redirect
from .models import Task

# 
def list_tasks(request):
    return render(request, 'list_tasks.html/')


#Create task
def create_task(request):
    """_CREATE TASK_
    This Function create a Task 
    Args:
        request: _Request_
    """
    
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')