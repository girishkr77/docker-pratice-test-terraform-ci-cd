from django.urls import path
from . import views

urlpatterns = [
    path('projects/',views.ProjectViewSet),
    path('task/<int:pk>/',views.Listviewset),
    path('delete/<int:pk>/',views.delete_task)

]