# MiniShop - E-commerce con Django

## Descripción
MiniShop es un e-commerce realizado durante mi curso de Django para aprender y practicar conceptos fundamentales de desarrollo Backend con este framework. Permite a los usuarios realizar pedidos de compras ficticias, recibir confirmaciones por correo electrónico y utilizar un sistema de inicio de sesión seguro.

## Características principales
- Sistema de autenticación de usuarios: Los usuarios pueden registrarse, iniciar sesión y cerrar sesión para realizar compras y acceder a funciones adicionales.
- Carrito de compras: Permite a los usuarios agregar y eliminar productos siempre que hayan iniciado sesión.
- Catálogo de productos: Muestra una lista de productos disponibles con detalles y precios.
- Procesamiento de pedidos: Los usuarios pueden realizar pedidos y recibir confirmaciones por correo electrónico.
- Envío de correos electrónicos: Se envían correos electrónicos de confirmación de pedidos a los usuarios y además los usuarios pueden contactarse.
- Administración de productos: Permite a los administradores agregar, editar y eliminar productos desde el panel de administración de Django.
- Administración de servicios: Permite a los administradores agregar, editar y eliminar servicios desde el panel de administración de Django.

## Instalación
1. Clona el repositorio: git clone https://github.com/17sTomy/minishop.git
2. Instala las dependencias necesarias: pip install -r requirements.txt
3. Crea un superusuario para acceder al panel de administración: python manage.py createsuperuser
4. Inicia el servidor de desarrollo: python manage.py runserver
5. Abre tu navegador y accede a http://127.0.0.1:8000/ para ver la aplicación en funcionamiento.

## Configuración del correo electrónico
Minishop utiliza el servicio de envío de correos electrónicos. Para que esta función funcione correctamente, configura las siguientes variables de entorno en tu entorno de desarrollo:

- EMAIL_HOST: El host del servidor de correo saliente.
- EMAIL_PORT: El puerto del servidor de correo saliente.
- EMAIL_HOST_USER: Tu dirección de correo electrónico.
- EMAIL_HOST_PASSWORD: Tu contraseña de correo electrónico.
- EMAIL_USE_TLS: Establece en True si se requiere TLS para conexiones seguras.