from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar/', views.agregarTarea, name='agregar_tarea'),
    path('editar/<int:tarea_id>/', views.editarTarea, name='editar_tarea'),
    path('eliminar/<int:tarea_id>/', views.eliminarTarea, name='eliminar_tarea'),
    path('actualizar/', views.actualizarTarea, name='actualizar_tarea'),  
    path('buscar/', views.buscar_tareas, name='buscar_tareas'),

]
