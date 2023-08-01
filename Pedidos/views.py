from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from Pedidos.models import LineaPedido, Pedido
from Carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags

# Create your views here.

@login_required(login_url="/autenticacion/login")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user) 
    carro = Carro(request)
    lineas_pedido = list()

    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido) # Lo almaceno en la bbdd

    enviar_mail(
        pedido = pedido,
        lineas_pedido = lineas_pedido,
        nombre_usuario = request.user.username,
        email_usuario = request.user.email
    )

    messages.success(request, "El pedido ha sido creado con éxito")
    carro.limpiar_carro()
    return redirect("../tienda/?valid")

def enviar_mail(**kwargs):
    subject = "Gracias por realizar el pedido."
    msg = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombre_usuario": kwargs.get("nombre_usuario")
    })

    msg_to_text = strip_tags(msg)
    from_email = "test_for_projects@outlook.com"
    to_email = kwargs.get("email_usuario")

    send_mail(subject, msg_to_text, from_email, [to_email], html_message=msg)
