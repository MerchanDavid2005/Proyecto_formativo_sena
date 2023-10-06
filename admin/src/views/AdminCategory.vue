<template>

  <AdminDefault>

    <div class="products-body">

      <CategorysAll />
      <FilterComp />

    </div>

  </AdminDefault>
  
</template>

<script setup>

  import AdminDefault from '@/layouts/adminDefault.vue'
  import CategorysAll from '@/components/CategorysAll.vue';
  import FilterComp from '@/components/FilterComp.vue'

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
