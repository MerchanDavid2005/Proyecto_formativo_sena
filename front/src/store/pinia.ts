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
  lista_productos: Producto [],
  fecha: string
    
}

export const useStore = defineStore('storeId', {
  state: () => {

    return {

      // Variables globales

      claro: true as boolean,
      productoVerificar: {} as Producto,
      idEliminar: 0,
      carrito: [] as Producto [],
      carritoFiltrar: [] as Producto [],
      usuario: 1,
      idPedido: {} as Pedido,

      // Lista informacion

      listaProductos: [] as Producto [],
      listaCategorias: [] as Categoria [],
      listaServicios: [] as Servicio [],
      listaPedidos: [] as Pedido [],

      // Lista informacion para filtrar

      listaProductosFiltrar: [] as Producto [],
      listaCategoriasFiltrar: [] as Categoria [],
      listaServiciosFiltrar: [] as Servicio [],

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

    async getPedidos(){

      const data = await fetch(`http://127.0.0.1:8000/get/orders/${this.usuario}/`)
      const info = await data.json()
      this.listaPedidos = info.pedidos
      console.log(this.listaPedidos)
    },

    async getPedidoId(id: string | string[]){

      const data = await fetch(`http://127.0.0.1:8000/get/order/${id}/`)
      const info = await data.json()
      this.idPedido = info.pedido

    },

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