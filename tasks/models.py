from django.db import models

class Task(models.model):
    name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return self.name
    
    