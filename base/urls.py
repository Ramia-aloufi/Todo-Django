from django.urls import path

from .views import TaskList,TaskDetails,TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetails.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('create-update/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('create-delete/<int:pk>/', TaskDelete.as_view(), name='delete-task'),




]