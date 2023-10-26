<template>
  <router-view/>
</template>

<script lang="ts" setup>

  import { useStore } from './store/pinia';
  import jwt_decode from 'jwt-decode'

  const pinia = useStore()

  import { onMounted } from 'vue';

  onMounted(() => {

    pinia.getProductos()
    pinia.getCategorias()
    pinia.getServicios()

    if(localStorage.getItem("token") !== null){

      const token:any = localStorage.getItem("token")
      const tokenDecodificado:any = jwt_decode(token);

      let fechaExpiracion = new Date(tokenDecodificado.exp)
      let hoy = new Date()
      
      if(fechaExpiracion <= hoy){

        localStorage.removeItem("token")
        
        setTimeout(() => {

          pinia.mensajeTokenCaducado = true

        }, 1000)

        setTimeout(() => {

          pinia.mensajeTokenCaducado = false

        }, 4000)

      }else{

        pinia.usuarioLogeado = true
        pinia.getUsuario(tokenDecodificado.id)

      }
 
    }

  })

</script>

<style lang="scss">

  *{

    padding: 0;
    margin: 0;
    font-family: sans-serif;

  }

  img{

    width: 100%;
    height: 100%;
    object-fit: contain;

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
