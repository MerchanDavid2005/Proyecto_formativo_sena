<template>
  <router-view/>
</template>

<script setup>

  import { useStore } from '@/store/pinia'
  import jwt_decode from 'jwt-decode'

  const pinia = useStore()

  async function traerTodo(){

    if(localStorage.getItem("token") !== null){

      const token = localStorage.getItem("token")
      const tokenDecodificado = jwt_decode(token);

      let fechaExpiracion = new Date(tokenDecodificado.exp)
      let hoy = new Date()

      if(fechaExpiracion <= hoy){

        localStorage.removeItem("token")

        setTimeout(() => {

          pinia.messagesSesionCaducada = true

        }, 1000)

        setTimeout(() => {
          
          pinia.messagesSesionCaducada = false

        }, 4000 );

      }else{

        pinia.getUsuario(tokenDecodificado.id)

      }

    }

    try{

      await pinia.getProductos();
      await pinia.getCategorias();
      await pinia.getServicios(),
      await pinia.getPedidos();
      await pinia.getUsuarios();

    }catch(e){

      setTimeout(() => {

        pinia.errorFetch = true

      }, 500)

      setTimeout(() => {

        pinia.errorFetch = false

      }, 3500)

    }

  }

  traerTodo()

</script>

<style lang="scss">

  *{

    padding: 0;
    margin: 0;
    font-family: sans-serif;
    box-sizing: border-box;

    img{

      width: 100%;
      height: 100%;
      object-fit: contain;

    }

  }

  ::-webkit-scrollbar {
    width: 10px;
    background-color: #f1f1f1;
  }

  ::-webkit-scrollbar-thumb {
    background-color: #888;
    border-radius: 5px;
  }


  ::-webkit-scrollbar-track {
    background-color: #f1f1f1;
  }

</style>
