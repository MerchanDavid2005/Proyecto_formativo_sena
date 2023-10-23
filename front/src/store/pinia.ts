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
  nombre: string,
  lista_productos: Producto [],
  fecha: string
    
}


type Usuario = {

  readonly id: number,
  nombre_usuario: string,
  nombre: string,
  email: string,
  foto: string,
  password: string,
  rol: string
}

type UsuarioCrear = {

  usuario: string,
  nombre: string,
  img: string,
  correo: string,
  password: string

}

export const useStore = defineStore('storeId', {
  state: () => {

    return {

      // Variables globales

      claro: true as boolean,
      
      productoVerificar: {} as Producto,
      idPedido: {} as Pedido,
      idEliminar: 0 as number,

      carrito: [] as Producto [],

      codigoVerificacion: "" as string,
      datosUsuarioCrear: {} as UsuarioCrear,
      mensajeUsuarioRegistrado: false as boolean,
      datosUsuario: {
        id: 1,
        nombre_usuario: "Anonimo",
        nombre: "Anonimo",
        email: "Anomimo@gmail.com",
        foto: "http://127.0.0.1:8000/media/usuarios/default.png",
        password: "Anonimo",
        rol: 'Cliente'
      } as Usuario,
      usuarioLogeado: false as boolean,
      datosUsuarioEditar: {} as Usuario,

      paginaActual: "",
  

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

    cambiarPagina(numeroPagina: number){

      this.listaProductosPagina = this.listaProductosFiltrar.slice(

        (numeroPagina - 1) * 12,
        numeroPagina * 12

      )

      this.paginaActual = `${numeroPagina}`

    },

    async getProductos(){

      const data = await fetch("http://127.0.0.1:8000/get/products/")
      const info = await data.json()
      this.listaProductos = info.productos.reverse()
      this.listaProductosFiltrar = this.listaProductos
      this.listaProductosPagina = this.listaProductos

    },

    async getPedidos(){

      const data = await fetch(`http://127.0.0.1:8000/get/orders/${this.datosUsuario.id}/`)
      const info = await data.json()
      this.listaPedidos = info.pedidos.reverse()
      this.listaPedidosFiltrar = this.listaPedidos

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

    async getUsuario(id: number){

      const data = await fetch(`http://127.0.0.1:8000/api/Usuario/${id}/`)
      const info = await data.json()
      this.datosUsuario = info

    }

  }

})