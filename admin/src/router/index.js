import { createRouter, createWebHistory } from 'vue-router'
import AdminProduct from '@/views/AdminProduct.vue'
import AdminCategory from '@/views/AdminCategory.vue'
import AdminService from '@/views/AdminService.vue'
import AdminOrder from '@/views/AdminOrder.vue'
import AdminUsers from '@/views/AdminUsers.vue'

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
    name: 'AdminOrder',
    component: AdminOrder
  },
  {
    path: '/admin/users',
    name: 'AdminUsers',
    component: AdminUsers
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
