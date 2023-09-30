import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import ProductoSerializer, CategoriaSerializer, UsuarioSerializer, PedidoSerializer, ServicioSerializer
from .models import Producto, Categoria, Usuario, Pedido, Servicio
from django.views.decorators.csrf import csrf_exempt

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

def traer_pedidos(request):

    pedidos = Pedido.objects.all()
    lista_pedidos = []
    for i in pedidos:
        lista_pedidos.append({"id" : i.id,
                              "pedido_usuario" : i.pedido_usuario.nombre_usuario,
                              "lista_productos" : i.lista_productos,
                              "fecha" : i.fecha})
    return JsonResponse({"productos" : lista_pedidos})

def traer_pedido_id(request, id):

    pedido = Pedido.objects.get(id = id)
    datos_pedido = {"id" : pedido.id,
                    "nombre" : pedido.nombre,
                    "descripcion" : pedido.descripcion,
                    "categoria" : pedido.categoria.nombre,
                    "cantidad" : pedido.cantidad,
                    "precio" : pedido.precio}
    return JsonResponse({"pedido" : datos_pedido})
