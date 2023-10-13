import json
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import ProductoSerializer, CategoriaSerializer, UsuarioSerializer, PedidoSerializer, ServicioSerializer
from .models import Producto, Categoria, Usuario, Pedido, Servicio
from django.views.decorators.csrf import csrf_exempt
import os
import random
from django.core.mail import send_mail
import jwt

class ProductoViewset(ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaViewset(ModelViewSet):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class UsuarioViewset(ModelViewSet):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PedidoViewset(ModelViewSet):

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ServicioViewset(ModelViewSet):

    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


# ----------------------------------------------- Endpoints de tabla productos ------------------------

@csrf_exempt
def crear_producto(request):

    cate = Categoria.objects.get(id = request.POST["categoria"])

    Producto.objects.create(

        nombre = request.POST["nombre"],
        categoria = cate,
        img = request.FILES.get("img"),
        descripcion = request.POST["descripcion"],
        cantidad = request.POST["cantidad"],
        precio = request.POST["precio"]

    )

    return HttpResponse ('Creado')

def traer_productos(request):

    productos = Producto.objects.all()
    lista_productos = []
    for i in productos:

        lista_productos.append({"id" : i.id,
                                "nombre" : i.nombre,
                                "descripcion" : i.descripcion,
                                "img": "http://127.0.0.1:8000/media/" + i.img.name,
                                "categoria" : i.categoria.nombre,
                                "cantidad" : i.cantidad,
                                "precio" : i.precio})
    return JsonResponse({"productos" : lista_productos})

def traer_producto_id(request, id):

    producto = Producto.objects.get(id = id)
    datos_producto = {"id" : producto.id,
                      "nombre" : producto.nombre,
                      "descripcion" : producto.descripcion,
                      "img": "http://127.0.0.1:8000/media/" + producto.img.name,
                      "categoria" : producto.categoria.nombre,
                      "cantidad" : producto.cantidad,
                      "precio" : producto.precio}
    return JsonResponse({"producto" : datos_producto})

@csrf_exempt
def actualizar_imagen_producto(request, id):

    producto = Producto.objects.get(id = id)

    producto.img = request.FILES.get("img")
    producto.save()

    return HttpResponse('Exito')

@csrf_exempt
def eliminar_imagen_producto(request, id):

    producto = Producto.objects.get(id = id)

    ruta_imagen = producto.img.name.split("/")
    img = os.path.join(settings.MEDIA_ROOT, ruta_imagen[1])

    if os.path.exists(img):

        os.remove(img)
        print("Imagen eliminada :D")

    else:

        print("Tas loco mi perro")

    return HttpResponse ("Exito")

# ----------------------------------------------- Endpoints de tabla servicios ------------------------

@csrf_exempt
def crear_servicio(request):

    Servicio.objects.create(

        nombre = request.POST["nombre"],
        img = request.FILES.get("img"),
        descripcion = request.POST["descripcion"],
        precio = request.POST["precio"]

    )

    return HttpResponse ('Creado')

@csrf_exempt
def actualizar_imagen_servicio(request, id):

    servicio = Servicio.objects.get(id = id)

    servicio.img = request.FILES.get('img')
    servicio.save()

    return HttpResponse ("Actualizado")

@csrf_exempt
def eliminar_imagen_servicio(request, id):

    servicio = Servicio.objects.get(id = id)

    ruta_imagen = servicio.img.name.split("/")
    img = os.path.join(settings.MEDIA_ROOT, ruta_imagen[1])

    if os.path.exists(img):

        os.remove(img)
        print("Imagen eliminada :D")

    else:

        print("Tas loco mi perro")

    return HttpResponse ("Exito")

# ----------------------------------------------- Endpoints de tabla pedidos ------------------------

def traer_todos_pedidos(request):

    pedidos = Pedido.objects.all()

    lista_pedidos = []

    for i in pedidos:

        lista_productos_pedido = []
        carrito = json.loads(i.lista_productos)

        for prd in carrito:

            lista_productos_pedido.append({
                "id": prd["id"],
                "nombre": prd["nombre"],
                "categoria": prd["categoria"],
                "img": prd["img"],
                "descripcion": prd["descripcion"],
                "cantidad": prd["cantidad"],
                "precio": prd["precio"]
            })

        lista_pedidos.append({
            "id": i.id,
            "nombre": i.pedido_usuario.nombre_usuario, 
            "lista_productos": lista_productos_pedido,
            "fecha": i.fecha
        })

    return JsonResponse({"pedidos" : lista_pedidos})

def traer_pedidos(request, id):

    pedidos = Pedido.objects.filter(pedido_usuario = id)

    lista_pedidos = []

    for i in pedidos:

        lista_productos_pedido = []
        carrito = json.loads(i.lista_productos)

        for prd in carrito:

            lista_productos_pedido.append({
                "id": prd["id"],
                "nombre": prd["nombre"],
                "categoria": prd["categoria"],
                "img": prd["img"],
                "descripcion": prd["descripcion"],
                "cantidad": prd["cantidad"],
                "precio": prd["precio"]
            })

        lista_pedidos.append({
            "id": i.id,
            "nombre": i.pedido_usuario.nombre_usuario, 
            "lista_productos": lista_productos_pedido,
            "fecha": i.fecha
        })

    return JsonResponse({"pedidos" : lista_pedidos})

def traer_pedido_id(request, id):

    pedido = Pedido.objects.get(id = id)

    datos_pedido = {}
    lista_productos = []

    carrito = json.loads(pedido.lista_productos)

    for i in carrito:

        lista_productos.append({
            "id": i["id"],
            "nombre": i["nombre"],
            "categoria": i["categoria"],
            "img": i["img"],
            "descripcion": i["descripcion"],
            "cantidad": i["cantidad"],
            "precio": i["precio"]
        })

    datos_pedido = {
        "usuario": pedido.pedido_usuario.nombre_usuario,
        "lista_productos": lista_productos,
        "fecha": pedido.fecha
    }

    return JsonResponse({"pedido" : datos_pedido})

# ----------------------------------------------- Endpoints de tabla usuarios ------------------------

@csrf_exempt
def crear_usuario_admin(request):

    avatar = ""

    if request.FILES.get("img") != None:

        avatar = request.FILES.get("img")
    
    else:

        avatar = os.path.join(settings.MEDIA_ROOT, "usuarios/default.png")

    Usuario.objects.create(

        nombre_usuario = request.POST["usuario"],
        nombre = request.POST["nombre"],
        email = request.POST["email"],
        foto = avatar,
        password = request.POST["password"],
        rol = "Administrador"
    )

    return HttpResponse ('Creado')

def traer_usuarios(request):

    usuarios = Usuario.objects.all()

    lista_usuario = []

    for i in usuarios:

        lista_usuario.append({

            "id": i.id,
            "usuario": i.nombre_usuario,
            "nombre": i.nombre,
            "email": i.email,
            "foto": "http://127.0.0.1:8000/media/" + i.foto.name,
            "rol": i.rol
        })

    return JsonResponse({"usuarios": lista_usuario})

@csrf_exempt
def eliminar_imagen_usuario(request, id):

    user = Usuario.objects.get(id = id)

    ruta_imagen = user.foto.name.split("/")
    img = os.path.join(settings.MEDIA_ROOT, ruta_imagen[0], ruta_imagen[1])

    imgDefault = os.path.join(settings.MEDIA_ROOT, "usuarios\default.png")

    if img != imgDefault:

        if os.path.exists(img):

            os.remove(img)
            print("Imagen eliminada :D")

        else:

            print("Tas loco mi perro")

    return HttpResponse ("Exito")

# ----------------------------------------------- Endpoints login ------------------------

clave_secreta = 'F9dyj4'

@csrf_exempt
def iniciar_sesion(request):

    usuarios = Usuario.objects.all()
    datos = json.loads(request.body)

    token = ""

    for i in usuarios:

        if i.nombre_usuario == datos["usuario"] and i.password == datos["password"]:

            payload={
                "usuario": datos["usuario"],
                "password": datos["password"]
            }

            token = jwt.encode(payload, clave_secreta, algorithm='HS256')

        else:

            token = "Error"

    return JsonResponse({"token": token})

@csrf_exempt
def enviar_correo_verificacion(request):

    datos_usuario = json.loads(request.body)
    nombre_usuario = datos_usuario["usuario"]
    email_usuario = datos_usuario["email"]

    lista_caracteres = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    codigo = ""

    caracteres = random.sample(lista_caracteres, k=6)

    for i in caracteres:

        codigo += i

    subject = 'Codigo de verificacion'
    message = "¡Bienvenido {}!, este es el ultimo paso para estar completamente registrado en servitca admin, solo necesitas copiar el siguiente codigo: {} y ponerlo en el campo correspondiente".format(nombre_usuario, codigo)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_usuario]

    send_mail(subject, message, email_from, recipient_list)

    return JsonResponse({"Codigo": codigo})