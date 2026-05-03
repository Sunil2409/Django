from celery import shared_task
import time

@shared_task
def simulate_heavy_work(task_id):
    time.sleep(10)
    from .models import Task
    task = Task.objects.get(id=task_id)
    task.status = "completed"
    task.save()