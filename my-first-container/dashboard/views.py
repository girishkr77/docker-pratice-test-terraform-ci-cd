from django.shortcuts import render
from .models import Project,Task
from django.http import HttpResponse
from dashboard.tasks import backgroung_worker

def ProjectViewSet(request):
    title = 'jai balaya'

    return render(request,'index.html',{'title':title})


def Listviewset(request,pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed
    task.save()
    backgroung_worker.delay()
    return HttpResponse('toggle switch')

def delete_task(request,pk):
    task = Task.objects.get(id = pk)
    task.delete()
    backgroung_worker.delay()

    return HttpResponse('deleted')




