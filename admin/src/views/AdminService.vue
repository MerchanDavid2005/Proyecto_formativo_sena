<template>

    <AdminDefault>
  
      <div class="products-body">
  
        <ServiceAll />
  
      </div>
  
    </AdminDefault>

</template>

<script setup>

import AdminDefault from '@/layouts/adminDefault.vue'
import ServiceAll from '@/components/ServiceAll.vue';

</script>

<style lang="scss" scoped>

.products-body{

    width: 100%;
    height: 100%;
    padding: 2%;
    display: flex;
    justify-content: space-between;
    overflow: auto;

}

</style>
  