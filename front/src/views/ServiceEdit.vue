<template>
    <MainDefault>

        <section class="cuerpo-editar-productos">

            <router-link class="contenedor-volver" :to="{name: 'datos'}">
                <v-icon name="bi-arrow-left-short" style="margin:10px 0;" scale="1.7"></v-icon> 
                <p> Volver </p> 
            </router-link>

            <ServiceSelected />
            <EditService />

        </section>

    </MainDefault>
</template>

<script lang="ts" setup>

    import MainDefault from '../layouts/MainDefault.vue'
    import EditService from '../components/EditService.vue';
    import ServiceSelected from '../components/ServiceSelected.vue'

</script>

<style lang="scss" scoped>

    .cuerpo-editar-productos{

        width: 100%;
        height: 90vh;
        display: flex;
        justify-content: space-evenly;
        align-items: center;

    }

    .contenedor-volver{

        position:absolute;
        top: 15%;
        left: 2%;
        padding: 0 10px;
        font-weight: bold;
        border-radius: 15px;
        background: $fondo-boton-limpiar;
        display: flex;
        align-items: center;
        text-decoration: none;
        color: #fff;

    }

</style>