from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from datetime import datetime

def home(request):
    tareas = Tarea.objects.all()
    return render(request, 'gestionTareas.html', {'listadoTareas': tareas})

def agregarTarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('txtTitulo')
        descripcion = request.POST.get('txtDescripcion')
        fecha_vencimiento_str = request.POST.get('txtFechaVencimiento')

        fecha_vencimiento = None
        if fecha_vencimiento_str:
            try:
                fecha_vencimiento = datetime.strptime(fecha_vencimiento_str, '%Y-%m-%d').date()
            except ValueError:
                return render(request, 'gestionTareas.html', {'listadoTareas': Tarea.objects.all(), 'mensaje': 'Formato de fecha inválido'})

        if not titulo:
            return render(request, 'gestionTareas.html', {'listadoTareas': Tarea.objects.all(), 'mensaje': 'El título no puede estar vacío'})

        Tarea.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            fecha_vencimiento=fecha_vencimiento,
            completada=False
        )

        return redirect('/')

    return redirect('/')

def editarTarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)

    if request.method == 'POST':
        if 'guardar_cambios' in request.POST:
            titulo = request.POST.get('txtTitulo')
            descripcion = request.POST.get('txtDescripcion')
            fecha_vencimiento_str = request.POST.get('txtFechaVencimiento')
            completada = request.POST.get('chkCompletada', False)

            if completada == 'on':
                completada = True
            else:
                completada = False

            fecha_vencimiento = None
            if fecha_vencimiento_str:
                try:
                    fecha_vencimiento = datetime.strptime(fecha_vencimiento_str, '%Y-%m-%d').date()
                except ValueError:
                    return render(request, 'editarTarea.html', {'tarea': tarea, 'mensaje': 'Formato de fecha inválido'})

            if not titulo:
                return render(request, 'editarTarea.html', {'tarea': tarea, 'mensaje': 'El título no puede estar vacío'})

            tarea.titulo = titulo
            tarea.descripcion = descripcion
            tarea.fecha_vencimiento = fecha_vencimiento
            tarea.completada = completada
            tarea.save()

            return redirect('/')  

        elif 'cancelar' in request.POST:
            return redirect('/')  

    return render(request, 'editarTarea.html', {'tarea': tarea})

def eliminarTarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    return redirect('/')

def actualizarTarea(request):
    if request.method == 'POST':
        tarea_id = request.POST.get('tarea_id')
        completada = request.POST.get('completada') == '1'

        tarea = get_object_or_404(Tarea, id=tarea_id)
        tarea.completada = completada
        tarea.save()

        return redirect('/')  

def buscar_tareas(request):
    query = request.GET.get('q')
    if query:
        tareas = Tarea.objects.filter(titulo__icontains=query)
    else:
        tareas = Tarea.objects.all()
    
    return render(request, 'resultados_busqueda.html', {'tareas': tareas, 'query': query})