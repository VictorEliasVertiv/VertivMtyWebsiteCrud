
# ./empleado/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.empleado_lista, name='empleados-lista'),
    path('crear/', views.crear_empleado, name='crear-empleado'),
    path('editar/<str:pk>/', views.editar_empleado, name='editar-empleado'),
    path('eliminar/<str:pk>/', views.eliminar_empleado, name='eliminar-empleado'),
]