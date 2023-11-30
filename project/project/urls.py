from django.urls import path
from app.views import ListTasksView,CreateTaskView,RetrieveTaskView,UpdateTaskView,DeleteTaskView,CreateUserView,ListUserView

urlpatterns = [    
    path('', ListTasksView.as_view(), name='list'),
    path('<int:pk>/', RetrieveTaskView.as_view(), name='retrieve'),
    path('create/', CreateTaskView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateTaskView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteTaskView.as_view(), name='delete'),
    
    
    path('create-user/',CreateUserView.as_view(),name='create-user'),
    path('check-user/',ListUserView.as_view(),name='check-user')
]