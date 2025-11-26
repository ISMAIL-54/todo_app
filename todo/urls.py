from django.urls import path
from . import views

# URLconf
urlpatterns = [
    path('home', views.task_list, name="task_list"),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_complete, name='toggle_complete'),
]