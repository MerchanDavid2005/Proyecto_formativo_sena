import { defineStore } from 'pinia'

export const useStore = defineStore('storeId', {
  state: () => {

    return {

      temaClaro: true,

      listaProductos: [],
      listaServicios: [],
      listaPedidos: [],
      listaCategorias: [],
      listaUsuarios: [],

      listaProductosFilter: [],
      listaServiciosFilter: [],
      listaPedidosFilter: [],
      listaCategoriasFilter: [],
      listaUsuariosFilter: [],

      idEliminar: 0,

      fondoFiltros: '#0af',
      greentheme: '#0fa',
      fondoEdits: '#fff',
      colorLetraPanel: '#fff',
      fondoRed: '#f05',

      datosUsuarioCrear: [],
      codigoVerificacion: "",
      mensajeUsuarioRegistrado: false,

      datosUsuarioIngresado: {

        nombre: "Nadie",
        email: "Nada",
        foto: "https://pbs.twimg.com/profile_images/1390430745705975811/PTN2XO5S_400x400.jpg"

      }

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

    },

    async getUsuario(id){

      const data = await fetch(`http://127.0.0.1:8000/api/Usuario/${id}/`)
      const info = await data.json()
      this.datosUsuarioIngresado = info

    },

    eliminar(modelo){

      fetch(`http://localhost:8000/api/${modelo}/${this.idEliminar}/`, {

        method: 'DELETE',
        headers: {"content-type" : "application/json"}

      });

      if(modelo == 'Producto'){

        fetch(`http://localhost:8000/delete/img/product/${this.idEliminar}/`);

      }else if(modelo == 'Servicio'){

        fetch(`http://localhost:8000/delete/img/service/${this.idEliminar}/`);

      }else{

        fetch(`http://localhost:8000/delete/img/user/${this.idEliminar}/`)

      }

    }

  }

})