import { defineStore } from 'pinia'

export const useStore = defineStore('storeId', {
  state: () => {

    return {

        listaProductos: [],
        listaServicios: [],
        listaPedidos: [],
        listaCategorias: [],
        listaUsuarios: [],

        listaProductosFilter: [],
        listaServiciosFilter: [],
        listaPedidosFilter: [],
        listaCategoriasFilter: [],
        listaUsuariosFilter: []

    }

  },
  actions: {

    async getProductos(){

        const data = await fetch("http://127.0.0.1:8000/get/products/")
        const info = await data.json()
        this.listaProductos = info.productos
        this.listaProductosFilter = this.listaProductos
  
    },
  
    async getPedidos(){
  
        const data = await fetch(`http://127.0.0.1:8000/get/orders/all/`)
        const info = await data.json()
        this.listaPedidos = info.pedidos
        this.listaPedidosFilter = this.listaPedidos
  
    },
  
    async getCategorias(){
  
        const data = await fetch("http://127.0.0.1:8000/api/Categoria/")
        const info = await data.json()
        this.listaCategorias = info
        this.listaCategoriasFilter = this.listaCategorias
  
    },
  
    async getServicios(){
  
        const data = await fetch("http://127.0.0.1:8000/api/Servicio/")
        const info = await data.json()
        this.listaServicios = info
        this.listaServiciosFilter = this.listaServicios
  
    },
  
    async getUsuarios(){
  
        const data = await fetch("http://127.0.0.1:8000/api/Usuario/")
        const info = await data.json()
        this.listaUsuarios = info
        this.listaUsuariosFilter = this.listaUsuarios
  
    }

  }

})