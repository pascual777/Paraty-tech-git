from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm  # Asume que tienes un formulario personalizado
from .models import UserConnection  
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Cambia aquí por tu formulario personalizado si es necesario
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Usuario creado correctamente.')
            return redirect('index')  # Asegúrate de que 'index' es la URL correcta
        else:
            # Este bucle recorre los errores y los agrega a los mensajes para mostrar en la plantilla
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en {field}: {error}")
    else:
        form = CustomUserCreationForm()  # Usa el formulario personalizado aquí también
    return render(request, 'add_user.html', {'form': form})

def add_connection(request, user_id):
    try:
        user_to = User.objects.get(id=user_id)
        UserConnection.objects.create(user_from=request.user, user_to=user_to)
        messages.success(request, "Conexión añadida correctamente.")
    except User.DoesNotExist:
        messages.error(request, "El usuario especificado no existe.")
    return redirect('index')  # Asegúrate de que 'index' es la URL correcta

def connected_users(request):
    connections = UserConnection.objects.all()
    return render(request, 'connected_users.html', {'connections': connections})


