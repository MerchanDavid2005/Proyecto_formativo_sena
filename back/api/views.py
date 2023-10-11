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

    img = 'C:/Users/lenovo/Desktop/Proyecto_formativo_David/back/media/' + producto.img.name

    if os.path.exists(img):

        os.remove(img)
        print("Imagen eliminada :D")

    else:

        print("Tas loco mi perro")

    return HttpResponse ("Exito")

# ----------------------------------------------- Endpoints de tabla productos ------------------------

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

@csrf_exempt
def eliminar_imagen_servicio(request, id):

    servicio = Servicio.objects.get(id = id)

    img = 'C:/Users/lenovo/Desktop/Proyecto_formativo_David/back/media/' + servicio.img.name

    if os.path.exists(img):

        os.remove(img)
        print("Imagen eliminada :D")

    else:

        print("Tas loco mi perro")

    return HttpResponse ("Exito")

# ----------------------------------------------- Endpoints de tabla usuarios ------------------------

def enviar_correo_verificacion(request):

    lista_caracteres = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    codigo = ""

    caracteres = random.sample(lista_caracteres, k=6)

    for i in caracteres:

        codigo += i

    return JsonResponse({"Codigo": codigo})


@csrf_exempt
def crear_usuario_admin(request):

    Usuario.objects.create(

        nombre_usuario = request.POST["usuario"],
        nombre = request.POST["nombre"],
        email = request.POST["email"],
        foto = request.FILES.get("img"),
        password = request.POST["descripcion"],
        rol = "Cliente"

    )

    return HttpResponse ('Creado')