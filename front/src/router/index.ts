import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import InicioView from '../views/InicioView.vue'
import CarritoView from '../views/CarritoView.vue'
import PerfilView from '../views/PerfilView.vue'
import ServiciosView from '../views/ServiciosView.vue'
import ContactoView from '../views/ContactoView.vue'
import PedidoIndividualView from '../views/PedidoIndividual.vue'
import IniciarSesionView from '../views/IniciarSesionView.vue'
import RegistrarseView from '../views/RegistrarseView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'productos',
    component: InicioView
  },
  {
    path: '/carrito',
    name: 'carrito',
    component: CarritoView
  },
  {
    path: '/perfil',
    name: 'perfil',
    component: PerfilView
  },
  {
    path: '/servicios',
    name: 'servicios',
    component: ServiciosView
  },
  {
    path: '/contacto',
    name: 'contacto',
    component: ContactoView
  },
  {
    path: '/pedido/:id',
    name: 'pedido',
    component: PedidoIndividualView
  },
  {
    path: '/iniciar_sesion',
    name: 'inicion/sesion',
    component: IniciarSesionView
  },
  {
    path: '/registrar',
    name: 'registrarse',
    component: RegistrarseView
  }
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
