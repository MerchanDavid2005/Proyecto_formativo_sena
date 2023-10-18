import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import InicioView from '../views/InicioView.vue'
import CarritoView from '../views/CarritoView.vue'
import PedidosView from '../views/PedidosView.vue'
import ServiciosView from '../views/ServiciosView.vue'
import ContactoView from '../views/ContactoView.vue'
import PedidoIndividualView from '../views/PedidoIndividual.vue'
import IniciarSesionView from '../views/IniciarSesionView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/productos/pagina/:id',
    name: 'productos',
    component: InicioView
  },
  {
    path: '/carrito',
    name: 'carrito',
    component: CarritoView
  },
  {
    path: '/pedidos',
    name: 'pedidos',
    component: PedidosView
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
    path: '/',
    name: 'inicion/sesion',
    component: IniciarSesionView
  }
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
