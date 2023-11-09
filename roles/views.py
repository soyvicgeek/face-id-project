from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from roles.models import Rol
from roles.forms import RolForm

# Create your views here.
def listar_usuario(request):
    # SELECT * FROM USUARIOS
    roles = Rol.objects.all()
    # Diccionario con las usuario
    return render(request,
                  'roles/rol_list.html', {'roles': roles})
def agregar_usuario(request):
    data = {
        'form': RolForm()
    }

    # Agregar la informción que se envio
    if request.method == 'POST':
        # Crear el formulario con los datos enviados
        formulario = RolForm(data=request.POST)
        # Validar la información
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado correctamente")
            return redirect(to='roles:rol_list')
        data['form'] = formulario

    return render(request, 'roles/rol_new.html', data )

def actualizar_usuario(request, id):
    rol = get_object_or_404(Rol, id=id)
    data = {
        'form': RolForm(instance=rol)
    }
    # Verificar si llego información por el método POST
    if request.method == 'POST':
        formulario = RolForm(data=request.POST, instance=rol)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Actualizado correctamente")
            return redirect(to='roles:rol_list')
        #Regresarle al formulario con lo errores al cliente
        data['form'] = formulario


    return render(request, 'roles/rol_update.html', data)

def eliminar_usuario(request, id):
    rol = get_object_or_404(Rol, id=id)
    rol.delete()
    return redirect(to='roles:rol_list')
