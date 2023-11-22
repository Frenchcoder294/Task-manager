from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('task/', views.task_list, name = 'task-list'),
    path('task/create/', views.create_task, name = 'create-task'),
    path('edit-task/<int:task_id>', views.edit_task, name = 'edit-task'),
    path('remove-task/<int:task_id>', views.remove_task, name = 'remove-task'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout')
]