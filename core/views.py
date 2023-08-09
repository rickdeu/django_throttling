from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from core.models import TodoList
from core.serializers import TodoListSerializer
from rest_framework.throttling import ScopedRateThrottle


class TodoListList(generics.ListCreateAPIView):
    throttle_scope = "todolist"
    throttle_classes = (ScopedRateThrottle, )
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    name = 'todolist-list'


class TodoListDetail(generics.RetrieveUpdateAPIView):
    throttle_scope = "todolist"
    throttle_classes = (ScopedRateThrottle, )
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    name = 'todolist-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response(
            {
                'todo-list': reverse(TodoListList.name, request=request)
            }
        )