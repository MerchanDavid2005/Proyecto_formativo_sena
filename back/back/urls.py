"""back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from api.router import router
from django.conf.urls.static import static
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('post/product/', views.crear_producto, name="Crear producto"),
    path('get/products/', views.traer_productos, name="Traer productos"),
    path('get/product/<int:id>/', views.traer_producto_id, name="Traer producto por id"),
    path('put/product/img/<int:id>/', views.actualizar_imagen_producto, name="Actualizar imagen producto"),
    path('post/service/', views.crear_servicio, name="Crear producto"),
    path('put/service/img/<int:id>/', views.actualizar_imagen_servicio, name="Actualizar imagen servicio"),
    path('get/orders/all/', views.traer_todos_pedidos, name="Traer todos los pedidos"),
    path('get/orders/<int:id>/', views.traer_pedidos, name="Traer pedidos"),
    path('get/order/<int:id>/', views.traer_pedido_id, name="Traer pedido por id")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)