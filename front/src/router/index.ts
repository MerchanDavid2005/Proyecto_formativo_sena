import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import InicioView from '../views/InicioView.vue'
import DatosView from '../views/DatosView.vue'
import CarritoView from '../views/CarritoView.vue'
import ServiciosView from '../views/ServiciosView.vue'
import ContactoView from '../views/ContactoView.vue'
import ProductEditView from '../views/ProductEditView.vue'
import ServiceEditView from '../views/ServiceEdit.vue'
import CategoryEditView from '../views/CategoryEditView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/productos/pagina/:id',
    name: 'productos',
    component: InicioView
  },
  {
    path: '/datos',
    name: 'datos',
    component: DatosView
  },
  {
    path: '/carrito',
    name: 'carrito',
    component: CarritoView
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
    path: '/producto/:id',
    name: 'producto',
    component: ProductEditView
  },
  {
    path: '/servicio/:id',
    name: 'servicio',
    component: ServiceEditView
  },
  {
    path: '/categoria/:id',
    name: 'categoria',
    component: CategoryEditView
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
