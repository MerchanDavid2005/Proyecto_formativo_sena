<template>

    <AdminDefault>
  
      <div :class="{'orders-body': !advertencia, 'orders-body-none': advertencia}">
  
        <h1 class="orders-body-title"> Pedidos </h1>
        <FilterOrder />
        <OrdersAll @eliminar="mostrar" />
  
      </div>

      <div class="interfaz">

        <transition>
  
          <DeleteConfirm 
            @cerrar="ocultar" 
            v-show="advertencia" 
            modelo="Pedido" 
            registro="este pedido" />
  
        </transition>
  
      </div>
  
    </AdminDefault>
    
</template>

<script setup>

  import AdminDefault from '@/layouts/adminDefault.vue'
  import OrdersAll from '@/components/OrdersAll.vue';
  import FilterOrder from '@/components/FilterOrder.vue'
  import DeleteConfirm from '@/components/DeleteConfirm.vue';

  import { ref } from 'vue';

  let advertencia = ref(false)

  const mostrar = () => advertencia.value = true

  const ocultar = () => advertencia.value = false
  
</script>

<style lang="scss" scoped>

  .orders-body{

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

  .orders-body-none{

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

  .v-enter-active, .v-leave-active{

    transition: all 2s cubic-bezier(1, -0.3, 0, 1.2);

  }

  .v-enter-from, .v-leave-to{

    transform: translateY(-800px);

  }

</style>
  