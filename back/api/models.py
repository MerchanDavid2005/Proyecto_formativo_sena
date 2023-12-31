from django.db import models

# Create your models here.

class Usuario(models.Model):

    nombre_usuario = models.CharField(max_length=50, null=False)
    nombre = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    foto = models.ImageField(upload_to='usuarios/')
    password = models.CharField(max_length=50, null=False)
    rol = models.CharField(max_length=50, null=False, default="Cliente")
    carrito = models.TextField(null=False)

class Categoria(models.Model):

    nombre = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):

    nombre = models.CharField(max_length=50, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    img = models.ImageField(upload_to='productos/')
    descripcion = models.TextField(null=False)
    cantidad = models.IntegerField(null=False)
    precio = models.FloatField(null=False)

class Pedido(models.Model):

    pedido_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    lista_productos = models.TextField(null=False)
    fecha = models.DateTimeField(auto_now_add=True)

class Servicio(models.Model):

    nombre = models.CharField(max_length=50, null=False)
    img = models.ImageField(upload_to='servicios/')
    descripcion = models.TextField(max_length=50, null=False)
    precio = models.FloatField(null=False)