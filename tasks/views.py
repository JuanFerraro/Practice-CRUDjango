from django.shortcuts import render, redirect
from .models import Task

# 
def list_tasks(request):   
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'list_tasks.html/', {'tasks': tasks})


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

#Delete task
def delete_task(request, task_id):
    """_DELETE TASK_

    Args:
        request: _Request_
        task_id (_id_): _This is the task's ID to delete_

    Returns:
        _Redirect to the main and only page_
    """

    delete_task = Task.objects.get(id=task_id)
    delete_task.delete()
    return redirect('/tasks/')
