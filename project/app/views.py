from .models import Task
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ListTasks,CreateUpdateTask,CreateUserSerializer,ListUserSerializer
from django.contrib.auth.models import User

class ListTasksView(ListAPIView):
    serializer_class = ListTasks
    queryset = Task.objects.all()

class RetrieveTaskView(RetrieveAPIView):
    serializer_class = ListTasks 
    lookup_field = 'pk'  

    def get_queryset(self):
        task_id = self.kwargs['pk']
        return Task.objects.filter(id=task_id)

class CreateTaskView(CreateAPIView):
    serializer_class = CreateUpdateTask

class UpdateTaskView(UpdateAPIView):
    serializer_class = CreateUpdateTask
    lookup_field = 'pk'  

    def get_queryset(self):
        task_id = self.kwargs['pk']
        return Task.objects.filter(id=task_id)
    
class DeleteTaskView(DestroyAPIView):
    serializer_class = ListTasks
    
    def get_queryset(self):
        task_id = self.kwargs['pk']
        return Task.objects.filter(id=task_id)
    
class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    
class ListUserView(ListAPIView):
    serializer_class = ListUserSerializer
    queryset = User.objects.all()