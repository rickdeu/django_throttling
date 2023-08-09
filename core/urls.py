from django.urls import path
from core import views
urlpatterns = [
    path(f'{views.TodoListList.name}/', views.TodoListList.as_view(), name=views.TodoListList.name),
    path(f'{views.TodoListDetail.name}/<int:pk>', views.TodoListDetail.as_view(), name=views.TodoListDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),

]
