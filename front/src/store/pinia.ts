import { defineStore } from 'pinia'

type Categoria = {

  readonly id: number,
  nombre: string

}

type Servicio = {

  readonly id: number,
  nombre: string,
  img: string,
  descripcion: string,
  precio: number

}

type Producto = {

  readonly id: number,
  nombre: string,
  descripcion: string,
  img: string,
  categoria: string,
  cantidad: number,
  precio: number

}

type Pedido = {

  readonly id: number,
  pedido_usuario: string,
  lista_productos: string,
  fecha: string
    
}

export const useStore = defineStore('storeId', {
  state: () => {

    return {

      // Variables globales

      claro: true,

      // Lista informacion

      listaProductos: [] as Producto [],
      listaCategorias: [] as Categoria [],
      listaServicios: [] as Servicio [],
      listaPedidos: [] as Pedido [],

      // Lista informacion para filtrar

      listaProductosFiltrar: [] as Producto [],
      listaCategoriasFiltrar: [] as Categoria [],
      listaServiciosFiltrar: [] as Servicio [],
      listaPedidosFiltrar: [] as Pedido [],

      // Lista productos por pagina

      listaProductosPagina: [] as Producto []
      
    }

  },
  actions: {

    async getProductos(){

      const data = await fetch("http://127.0.0.1:8000/get/products/")
      const info = await data.json()
      this.listaProductos = info.productos.reverse()
      this.listaProductosFiltrar = this.listaProductos
      this.listaProductosPagina = this.listaProductos

    },

    // async getPedidos(){

    //   const data = await fetch("http://127.0.0.1:8000/get/orders/")
    //   const info = await data.json()
    //   this.listaPedidos = info.pedidos

    // },

    async getCategorias(){

      const data = await fetch("http://127.0.0.1:8000/api/Categoria/")
      const info = await data.json()
      this.listaCategorias = info.reverse()
      this.listaCategoriasFiltrar = this.listaCategorias

    },

    async getServicios(){

      const data = await fetch("http://127.0.0.1:8000/api/Servicio/")
      const info = await data.json()
      this.listaServicios = info.reverse()
      this.listaServiciosFiltrar = this.listaServicios

    },

  }

})