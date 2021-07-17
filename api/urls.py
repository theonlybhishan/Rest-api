from django.urls import path
from django.urls.resolvers import URLPattern
from .import views

urlpatterns =[
    path('', views.apiOvervew, name= "api-overview"),
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<str:pk>/', views.taskDetail, name='task-detail'),    
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>/', views.taskCreate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
]