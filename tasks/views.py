from django.shortcuts import render,redirect
from .models import Task
from .tasks import simulate_heavy_work

def task_list():
    if request.method == "POST":
        name = request.POST.get("name")
        task = Task.objects.create(name=name)
        simulate_heavy_work.delay(task.id)
        return redirect (task_list)

    tasks = Task.objects.all().order_by('_created_at')
    return render(request, 'tasks/list.html',{'tasks':tasks})