from django.urls import path
from . import views

# URLconf
urlpatterns = [
    path('home', views.task_list, name="task_list")
]