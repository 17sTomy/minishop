from django.shortcuts import render, redirect
from django.views.generic import View
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField() 

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class VRegistro(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "registro/registro.html", {"form": form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("Home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", {"form": form})
        
def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) # Incializa el formulario con esos datos
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.error(request, "Usuario y/o Contraseña Incorrecto/s")
        else:
            messages.error(request, "Usuario y/o Contraseña Incorrecto/s")

    form = AuthenticationForm()
    return render(request, "login/login.html", {"form": form})
        
def cerrar_sesion(request):
    logout(request)
    return redirect('Home')