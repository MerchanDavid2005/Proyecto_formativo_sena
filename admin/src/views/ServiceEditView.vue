<template>
    
    <AdminDefault>

        <div class="body-service-edit">

            <button
                :style="{background: pinia.fondoFiltros}"
                @click="enrutado.push('/admin/service')" 
                class="body-service-edit-volver"> Volver 
            </button>
            <ServiceSelected />
            <EditService />

        </div>

    </AdminDefault>    

</template>

<script setup>

    import AdminDefault from '@/layouts/adminDefault.vue';
    import EditService from '@/components/EditService.vue';
    import ServiceSelected from '@/components/ServiceSelected.vue';

    import { useRouter } from 'vue-router';
    import { useStore } from '@/store/pinia';

    const pinia = useStore()
    const enrutado = useRouter()

</script>

<style lang="scss" scoped>

    .body-service-edit{

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