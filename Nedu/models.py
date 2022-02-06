from django.db import connections
from django.db import models

class TasksDetails(models.Model):
    name = models.CharField(max_length=40)
    priority = models.CharField(max_length=20)
    class Meta:
        db_table = "tasks"