<template>

  <AdminDefault>

    <div :class="{'services-body' : !advertencia, 'services-body-none': advertencia}">

      <h1 class="services-body-title"> Servicios </h1>
      <FilterService />
      <ServiceAll @eliminar="mostrar" />

    </div>

    <div class="interfaz">

      <transition name="transicionServiceDanger">

        <DeleteConfirm 
          @cerrar="ocultar" 
          v-show="advertencia" 
          modelo="Servicio" 
          registro="este servicio" />

      </transition>

    </div>

  </AdminDefault>

</template>

<script setup>

  import AdminDefault from '@/layouts/adminDefault.vue';
  import FilterService from '@/components/FilterService.vue';
  import ServiceAll from '@/components/ServiceAll.vue';
  import DeleteConfirm from '@/components/DeleteConfirm.vue';

  import { ref } from 'vue';
  import { useRouter } from 'vue-router';

  const enrutado = useRouter()

  let advertencia = ref(false)

  const mostrar = () => advertencia.value = true

  const ocultar = () => advertencia.value = false

  if(localStorage.getItem('token') == "Error" || localStorage.getItem("token") == null){

    enrutado.push('/')

  }


</script>

<style lang="scss" scoped>

  .services-body{

    width: 100%;
    height: 100%;
    padding: 2%;
    display: flex;
    flex-direction: column;
    filter: brightness(100%);
    background: transparent;
    pointer-events: all;
    overflow: auto;
    position: static;
    z-index: 1000;
    transition: all 0.5s ease-in-out;
    
    &-title{

      font-size: 50px;
      margin-bottom: 10vh;
      text-align: center;

    } 

  }

  .services-body-none{

    width: 100%;
    height: 100%;
    padding: 2%;
    display: flex;
    flex-direction: column;
    filter: brightness(20%);
    background: #444;
    pointer-events: none;
    overflow: hidden;
    position: static;
    z-index: 1000;
    transition: all 0.5s ease-in-out;

  }

  .interfaz{

    width: 100%;
    height: 90%;
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;

  }

  .transicionServiceDanger-enter-active, .transicionServiceDanger-leave-active{

    transition: all 2s cubic-bezier(1, -0.3, 0, 1.2);

  }

  .transicionServiceDanger-enter-from, .transicionServiceDanger-leave-to{

    transform: translateY(-800px);

  }

</style>
  