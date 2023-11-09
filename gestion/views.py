from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'usuarios/usuario_list.html')
    #return render(req, 'gestion/index.html')

def dashboard(req):
    return render(req, 'gestion/dashboard.html')