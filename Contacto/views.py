from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import send_mail, EmailMessage

# Create your views here.

def contacto(request):
    form_contacto = FormularioContacto()

    if request.method == 'POST':
        form_contacto = FormularioContacto(data=request.POST)
        if form_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde Django",
            f"Usuario: {nombre}\nE-mail: {email}\nEscribe: {contenido}",
            "",
            ["test_for_projects@outlook.com"],
            reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valid")
            except:
                return redirect("/contacto/?invalid")

    return render(request, "contacto/contacto.html", {"form": form_contacto})