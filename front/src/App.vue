<template>
  <router-view/>
</template>

<script lang="ts" setup>

  import { useStore } from './store/pinia';

  const pinia = useStore()

  import { onMounted } from 'vue';

  onMounted(() => {

    // pinia.getPedidos()
    pinia.getProductos()
    pinia.getCategorias()
    pinia.getServicios()

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
