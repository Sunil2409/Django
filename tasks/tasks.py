from celery import shared_task
import time

@shared_task

def simulate_heavy_work():
    time.sleep(10)
    from .models import Task
    task = Task.objects.get(id=Task_id)
    task.status = "completed"
    task.save()