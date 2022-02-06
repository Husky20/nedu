from django.shortcuts import render
from Nedu.models import TasksDetails

def showTasks(request):
    resultsdisplay = TasksDetails.objects.all()
    return render(request, "Tasks.html", {'TasksDetails': resultsdisplay})