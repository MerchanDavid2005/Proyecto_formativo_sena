<template>
    <MainDefault>

        <div class="interfaz-eliminar">

            <transition>
                
                <VerifyDelete 
                @ocultar="ocultarInterfaz"
                v-show="eliminarProducto" 
                texto="¿Estas seguro de querer eliminar este producto del carrito?" />

            </transition>

        </div>

        <main :class="{'cuerpo-carrito-view': funcionando, 'cuerpo-none' : !funcionando}">

            <CarAll @eliminar="eliminacionProducto" />
            <FilterData />

        </main>

    </MainDefault>
</template>

<script lang="ts" setup>

    import MainDefault from '../layouts/MainDefault.vue'
    import FilterData from '../components/FilterData.vue';
    import CarAll from '../components/CarAll.vue'
    import VerifyDelete from '../components/VerifyDelete.vue';

    import { ref } from 'vue';

    let eliminarProducto = ref<boolean>(false)
    let funcionando = ref<boolean>(true)

    const eliminacionProducto = () => {

        eliminarProducto.value = true
        funcionando.value = false

    }

    const ocultarInterfaz = () => {

        eliminarProducto.value = false
        funcionando.value = true

    }

</script>

<style lang="scss" scoped>

    .cuerpo-carrito-view{

        position: static;
        z-index: 5000;
        width: 100%;
        height: 85vh;
        padding-top: 5vh;
        display: flex;
        justify-content: space-around;
        overflow: auto;
        filter: blur(0px);
        pointer-events: all;

    }

    .cuerpo-none{

        position: static;
        z-index: 5000;
        width: 100%;
        height: 85vh;
        padding-top: 5vh;
        display: flex;
        justify-content: space-around;
        overflow: auto;
        filter: blur(7px);
        pointer-events: none;
        overflow: hidden;

    }

    .interfaz-eliminar{

        width: 100%;
        height: 85vh;
        display: flex;
        justify-content: center;
        align-items: center;
        position: absolute;

    }

    .v-enter-active, .v-leave-active{

        transition: transform 0.5s ease-in-out;

    }

    .v-enter-from, .v-leave-to{

        transform: scale(0.1);

    }

</style>