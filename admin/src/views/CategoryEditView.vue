<template>
    
    <AdminDefault>

        <div class="body-category-edit">

            <button 
                :style="{background: pinia.fondoFiltros}"
                @click="enrutado.push('/admin/category')" 
                class="body-category-edit-volver"> Volver 
            </button>
            <EditCategory />
            <CategorySelected />

        </div>

    </AdminDefault>    

</template>

<script setup>

    import AdminDefault from '@/layouts/adminDefault.vue';
    import EditCategory from '@/components/EditCategory.vue';
    import CategorySelected from '@/components/CategorySelected.vue';

    import { useRouter } from 'vue-router';
    import { useStore } from '@/store/pinia';

    const pinia = useStore()
    const enrutado = useRouter()

    if(localStorage.getItem('token') == "error" || localStorage.getItem("token") == null){

        enrutado.push('/')

    }

</script>

<style lang="scss" scoped>

    .body-category-edit{

        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-evenly;

        &-volver{

            position: absolute;
            left: 2%;
            top: 10%;
            @include botones();

        }

    }

</style>