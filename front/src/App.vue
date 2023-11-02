<template>
  <router-view/>
</template>

<script lang="ts" setup>

  import { useStore } from './store/pinia';
  import jwt_decode from 'jwt-decode'
  import { useRouter } from 'vue-router'

  const enrutado = useRouter()
  const pinia = useStore()

  async function inicializar(){

    pinia.pantallaCarga = true

    try{

      await pinia.cargarDatos()

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
          await pinia.getUsuario(tokenDecodificado.id)   

        }

      }

      pinia.pantallaCarga = false
      sessionStorage.setItem("error", "false")

    }catch(e){

      pinia.pantallaCarga = false
      sessionStorage.setItem("error", "true")
      enrutado.push('/error')

    }

  }

  inicializar()

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
