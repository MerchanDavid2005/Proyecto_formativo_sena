import { createRouter, createWebHistory } from 'vue-router'
import AdminProduct from '@/views/AdminProduct.vue'
import AdminCategory from '@/views/AdminCategory.vue'
import AdminService from '@/views/AdminService.vue'
import AdminOrder from '@/views/AdminOrder.vue'
import AdminUsers from '@/views/AdminUsers.vue'
import ProductEditView from '@/views/ProductEditView.vue'
import ServiceEditView from '@/views/ServiceEditView.vue'
import CategoryEditView from '@/views/CategoryEditView.vue'

const routes = [
  {
    path: '/admin/product',
    name: 'adminProduct',
    component: AdminProduct
  },
  {
    path: '/admin/category',
    name: 'adminCategory',
    component: AdminCategory
  },
  {
    path: '/admin/service',
    name: 'adminService',
    component: AdminService
  },
  {
    path: '/admin/order',
    name: 'adminOrder',
    component: AdminOrder
  },
  {
    path: '/admin/users',
    name: 'adminUsers',
    component: AdminUsers
  },
  {
    path: '/admin/edit/product/:id',
    name: 'adminEditProduct',
    component: ProductEditView
  },
  {
    path: '/admin/edit/service/:id',
    name: 'adminEditService',
    component: ServiceEditView
  },
  {
    path: '/admin/edit/category/:id',
    name: 'adminEditCategory',
    component: CategoryEditView
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
