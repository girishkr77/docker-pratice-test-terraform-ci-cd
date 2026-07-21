from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Project)
class projectAdmin(admin.ModelAdmin):
    list_display = ['name','owner_name']
    search_fields = ['name']

@admin.register(models.Task)
class taskAdmin(admin.ModelAdmin):
    list_display = ['title','completed','project','description']
    autocomplete_fields = ['project']