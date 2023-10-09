<template>
    
    <AdminDefault>

        <div class="body-product-edit">

            <button
                :style="{background: pinia.fondoFiltros}"
                @click="enrutado.push('/admin/product')" 
                class="body-product-edit-volver"> Volver 
            </button>
            <ProductSelected />
            <EditProduct />

        </div>

    </AdminDefault>    

</template>

<script setup>

    import AdminDefault from '@/layouts/adminDefault.vue'
    import ProductSelected from '@/components/ProductSelected.vue';
    import EditProduct from '@/components/EditProduct.vue';

    import { useRouter } from 'vue-router';
    import { useStore } from '@/store/pinia';

    const pinia = useStore()
    const enrutado = useRouter()

</script>

<style lang="scss" scoped>

    .body-product-edit{

        width: 100%;
        height: 100%;
        display: flex;
        justify-content: space-evenly;
        align-items: center;

        &-volver{

            position: absolute;
            left: 2%;
            top: 10%;
            @include botones();

        }

    }

</style>