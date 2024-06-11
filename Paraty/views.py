from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm  
from .models import UserConnection  
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Usuario creado correctamente.')
            return redirect('index')  
        else:
            
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en {field}: {error}")
    else:
        form = CustomUserCreationForm()  
    return render(request, 'add_user.html', {'form': form})

def add_connection(request, user_id):
    try:
        user_to = User.objects.get(id=user_id)
        UserConnection.objects.create(user_from=request.user, user_to=user_to)
        messages.success(request, "Conexión añadida correctamente.")
    except User.DoesNotExist:
        messages.error(request, "El usuario especificado no existe.")
    return redirect('index')  

def connected_users(request):
    connections = UserConnection.objects.all()
    return render(request, 'connected_users.html', {'connections': connections})

def register_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  
    else:
        form = ContactForm()
    return render(request, 'register_contact.html', {'form': form})

