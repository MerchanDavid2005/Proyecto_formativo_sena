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
from django.core.mail import EmailMessage
from datetime import datetime, timedelta
from fpdf import FPDF
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

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

    ruta_imagen = producto.img.name.split("/")
    img = os.path.join(settings.MEDIA_ROOT, ruta_imagen[0], ruta_imagen[1])

    producto.img = request.FILES.get("img")
    producto.save()

    if os.path.exists(img):

        os.remove(img)
        print("Imagen eliminada :D")

    else:

        print("Tas loco mi perro")

    return HttpResponse('Exito')

@csrf_exempt
def eliminar_imagen_producto(request, id):

    producto = Producto.objects.get(id = id)

    ruta_imagen = producto.img.name.split("/")
    img = os.path.join(settings.MEDIA_ROOT, ruta_imagen[0], ruta_imagen[1])

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

    ruta_imagen = servicio.img.name.split("/")
    img = os.path.join(settings.MEDIA_ROOT, ruta_imagen[0], ruta_imagen[1])
    servicio.img = request.FILES.get('img')
    servicio.save()


    if os.path.exists(img):

        os.remove(img)
        print("Imagen eliminada :D")

    else:

        print("Tas loco mi perro")

    return HttpResponse ("Actualizado")

@csrf_exempt
def eliminar_imagen_servicio(request, id):

    servicio = Servicio.objects.get(id = id)

    ruta_imagen = servicio.img.name.split("/")
    img = os.path.join(settings.MEDIA_ROOT, ruta_imagen[0], ruta_imagen[1])

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
def crear_usuario(request, rol):

    avatar = ""

    if request.FILES.get("img") != None:

        avatar = request.FILES.get("img")
    
    else:

        avatar = "usuarios/default.png"

    if rol == "Admin":

        Usuario.objects.create(

            nombre_usuario = request.POST["usuario"],
            nombre = request.POST["nombre"],
            email = request.POST["email"],
            foto = avatar,
            password = request.POST["password"],
            rol = "Administrador"
        )
    
    else:

        Usuario.objects.create(

            nombre_usuario = request.POST["usuario"],
            nombre = request.POST["nombre"],
            email = request.POST["email"],
            foto = avatar,
            password = request.POST["password"],
            rol = "Cliente"
        )

    return HttpResponse ('Creado')

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

    return JsonResponse({"Mensaje": "Imagen eliminada"})

@csrf_exempt
def actualizar_usuario(request, id):

    usuario = Usuario.objects.get(id = id)

    mensaje = ""

    usuario.nombre_usuario = request.POST["usuario"]
    usuario.nombre = request.POST["nombre"]
    usuario.email = request.POST["email"]

    if request.FILES.get("img") != None:
             
        ruta_imagen = usuario.foto.name.split("/")
        img = os.path.join(settings.MEDIA_ROOT, ruta_imagen[0], ruta_imagen[1])  
        usuario.foto = request.FILES.get("img")

        imgDefault = os.path.join(settings.MEDIA_ROOT, "usuarios\default.png")

        if img != imgDefault:

            if os.path.exists(img):

                os.remove(img)
                print("Imagen eliminada :D")

            else:

                print("Tas loco mi perro")

    usuario.save()

    mensaje = "¡Actualizado!"


    return JsonResponse({"Mensaje": mensaje})

    

# ----------------------------------------------- Endpoints login ------------------------

clave_secreta = 'F9dyj4'

@csrf_exempt
def iniciar_sesion(request, rol):

    usuarios = Usuario.objects.filter(rol = rol)
    datos = json.loads(request.body)

    token = ""

    hoy = datetime.now()
    fechaExpiracion = hoy + timedelta(days=7)
    fechaExpiracion_token = fechaExpiracion.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    for i in usuarios:

        if i.nombre_usuario == datos["usuario"] and i.password == datos["password"]:

            payload={
                "id": i.id,
                "exp": fechaExpiracion_token
            }

            token = jwt.encode(payload, clave_secreta, algorithm='HS256')
            break

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

    asunto = 'Codigo de verificacion'
    mensaje = """

    <html>
        <body>
            <div style='padding:30px; height:300px; background:#eee; border-radius:30px'>

                <h1 style='text-align:center; font-size:45px;'> ¡Bienvenid@ {}! </h1> 
                <p style='font-size:15px;'> Este es el ultimo paso para estar completamente registrado en serviteca la estacion, solo necesitas copiar el siguiente codigo e ingresarlo en el campo correspondiente </p>
                <p style='text-align:center; font-weight:bold; font-size:40px;'> 
                    Codigo: <span> {} </span> 
                </p>

            </div>
        </body>
    <html>
    """.format(nombre_usuario, codigo)
    emisor = settings.EMAIL_HOST_USER
    remitente = [email_usuario]

    send_mail(
        asunto, 
        '', 
        emisor,
        remitente,
        html_message=mensaje
    )

    return JsonResponse({"Codigo": codigo})

@csrf_exempt
def guardar_imagen_correo(request):

    image = request.FILES.get("imagen")

    file_path = os.path.join(settings.MEDIA_ROOT, 'correos', image.name)
    
    with open(file_path, 'wb') as destination:
        for chunk in image.chunks():
            destination.write(chunk)

    return JsonResponse({"Mensaje": "Imagen guardada exitosamente"})

@csrf_exempt
def enviar_correo_contacto(request):

    asunto = '{} - {}'.format(request.POST["nombre"] ,request.POST["motivo"])
    mensaje = "{}".format(request.POST["descripcion"])
    remitente = settings.EMAIL_HOST_USER
    destinatario = ["pipebarret7@gmail.com"]

    nombre_imagen = request.FILES.get("imagen").name

    directorio_medios = os.path.join(settings.MEDIA_ROOT, 'correos')

    ruta = ""

    for imgs in os.listdir(directorio_medios):

        if os.path.join(directorio_medios, imgs) == os.path.join(directorio_medios, nombre_imagen):

            ruta = os.path.join(directorio_medios, imgs)

    email = EmailMessage(asunto, mensaje, remitente, destinatario)
    email.attach_file(ruta)
    email.send()

    return HttpResponse("Enviado")

@csrf_exempt
def generar_factura(request):

    id = request.POST["id"]
    usuario = request.POST["usuario"]
    nombre = request.POST["nombre"]
    correo = request.POST["correo"]
    data = datetime.now()
    fecha = data.strftime("%d-%m-%Y %H:%M:%S")
    carrito = request.POST["carrito"]

    productos = json.loads(carrito)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=30)
    pdf.cell(200, 30, txt="Datos del pedido", ln=1, align="C")
    pdf.set_font("Arial", size=20)
    pdf.cell(200, 20, txt="Serviteca la estacion", ln=1)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 15, txt="---------------------------------------------------------------------------------------------------------------------------------", ln=1)
    pdf.cell(200, 10, txt="Usuario: {}".format(usuario), ln=1)
    pdf.cell(200, 10, txt="Nombre: {}".format(nombre), ln=1)
    pdf.cell(200, 10, txt="Correo: {}".format(correo), ln=1)
    pdf.cell(200, 10, txt="Fecha: {}".format(fecha), ln=1)
    pdf.cell(200, 15, txt="---------------------------------------------------------------------------------------------------------------------------------", ln=1)

    total_pedido = 0

    ruta = os.path.join(settings.MEDIA_ROOT, "facturas/Factura_{}_{}.pdf".format(usuario, id))
    
    for i in productos:

        precio = locale.format_string("%d", i["precio"], grouping=True)
        pdf.cell(80, 15, txt="Producto: {}".format(i["nombre"]), ln=0)
        pdf.cell(50, 15, txt="Unidades: {}".format(i["cantidad"]), ln=0)
        pdf.cell(65, 15, txt="Total: {}".format(precio), ln=1)
        total_pedido += i["precio"]

    total_precio = locale.format_string("%d", total_pedido, grouping=True)

    pdf.cell(200, 15, txt="---------------------------------------------------------------------------------------------------------------------------------", ln=1)
    pdf.cell(200, 15, txt="Total valor del pedido: {}".format(total_precio), ln=1)
    pdf.output(os.path.join(ruta))

    return JsonResponse({"Mensaje": "¡Creado!"})

@csrf_exempt
def enviar_factura(request):

    datosUsuario = json.loads(request.body)

    factura = os.path.join(settings.MEDIA_ROOT, "facturas/factura_{}_{}.pdf").format(datosUsuario["usuario"], datosUsuario["id"])

    if os.path.exists(factura):

        asunto = "Factura_{}_{}".format(datosUsuario["usuario"], datosUsuario["id"])
        mensaje = """ Gracias por tu compra {}, esperamos que sigas comprando en nuestra pagina web, aqui esta la factura de tu compra""".format(datosUsuario["usuario"])
        emisor = settings.EMAIL_HOST_USER
        remitente = [datosUsuario["email"]]
        correo = EmailMessage(asunto, mensaje, emisor, remitente)
        correo.content_subtype = "html"
        html_content = """
            <html>

                <body>

                    <div style='padding:30px; height:300px; background:#eee; border-radius:30px'>

                        <h1 style='text-align:center; font-size:45px;'> Gracias por tu compra </h1>

                        <p style='font-size:15px;'> Gracias por tu compra {}, esperamos que sigas comprando en nuestra pagina web </p>
                        <p style='font-size:15px;'> Aqui esta la factura de tu compra: </p>

                    </div>

                </body>

            </html>

        """.format(datosUsuario["usuario"])
        correo.body = html_content
        correo.attach_file(factura)
        correo.send()

    return JsonResponse({"mensaje": "¡Enviado!"})

