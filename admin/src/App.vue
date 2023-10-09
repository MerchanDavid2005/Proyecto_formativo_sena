<template>
  <transition name="transitionViews">
    <router-view/>
  </transition>
</template>

<script setup>

  import { onMounted } from 'vue'
  import { useStore } from '@/store/pinia'

  const pinia = useStore()

  onMounted(() => {

    pinia.getProductos();
    pinia.getCategorias();
    pinia.getServicios(),
    pinia.getPedidos();
    pinia.getUsuarios();

  })

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

  .transitionViews-enter-active, .transitionViews-leave-active{

    transition: opacity 0.5s cubic-bezier(1, 1, 1, 1);

  }

  .transitionViews-enter-from, .transitionViews-leave-to{

    opacity: 0;

  }

</style>
