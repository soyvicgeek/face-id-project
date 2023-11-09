from django.shortcuts import render, redirect, get_object_or_404
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm

# Create your views here.
def listar_usuario(request):
    # SELECT * FROM USUARIOS
    usuarios = Usuario.objects.all()
    # Diccionario con las usuario
    return render(request,
                  'usuarios/usuario_list.html', {'usuarios': usuarios})
def agregar_usuario(request):
    data = {
        'form': UsuarioForm()
    }

    # Agregar la informción que se envio
    if request.method == 'POST':
        # Crear el formulario con los datos enviados
        formulario = UsuarioForm(data=request.POST)
        # Validar la información
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Usuario guardada'
        else:
            data['form'] = formulario

    return render(request, 'usuarios/usuario_new.html', data )

def actualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    data = {
        'form': UsuarioForm(instance=usuario)
    }
    # Verificar si llego información por el método POST
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='usuarios:usuario_list')
        #Regresarle al formulario con lo errores al cliente
        data['form'] = formulario


    return render(request, 'usuarios/usuario_update.html', data)

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect(to='usuarios:usuario_list')