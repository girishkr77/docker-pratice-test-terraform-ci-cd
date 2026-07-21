from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    project= models.ForeignKey(Project,on_delete=models.PROTECT,related_name='task',default=None)
    description = models.TextField(default='description',blank=True)

    def __str__(self):
        return self.title

    
