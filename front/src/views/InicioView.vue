<template>
    <MainDefault>

        <div class="contenedor-compras">

            <ProductsAll />
            <FilterData />

        </div>

    </MainDefault>
</template>

<script lang="ts" setup>

    import MainDefault from '../layouts/MainDefault.vue'
    import ProductsAll from '../components/ProductsAll.vue'
    import FilterData from '../components/FilterData.vue';

</script>

<style lang="scss" scoped>

    .contenedor-compras{

        width: 100%;
        height: 85vh;
        display: flex;
        justify-content: space-around;
        padding-top: 5vh;
        overflow: auto;

    }

</style>