<template>
    <MainDefault>

        <div class="interfaz-eliminar">

            <transition name="messages">

                <component 
                    v-show="mensajeMostrar" 
                    @ocultar="ocultarMensaje" 
                    :is="tipoMensaje"
                    texto="¿Estas seguro de querer eliminar este producto del carrito?">
                </component>

            </transition>

        </div>

        <main :class="{'cuerpo-carrito-view': !mensajeMostrar, 'cuerpo-none' : mensajeMostrar}">

            <CarAll @eliminar="mostrarMensaje" />

        </main>

    </MainDefault>
</template>

<script lang="ts" setup>

    import MainDefault from '../layouts/MainDefault.vue';
    import CarAll from '../components/CarAll.vue';

    import { ref, defineAsyncComponent, shallowRef } from 'vue';

    let mensajeMostrar = ref<boolean>(false)

    const mensajeCreado = defineAsyncComponent(() => import('../components/OrderExit.vue'))

    let tipoMensaje = shallowRef(mensajeCreado)

    const mostrarMensaje = (mensaje: any) => {

        mensajeMostrar.value = true
        tipoMensaje.value = mensaje

    }

    const ocultarMensaje = () => mensajeMostrar.value = false

</script>

<style lang="scss" scoped>

    .cuerpo-carrito-view{

        position: static;
        z-index: 5000;
        width: 100%;
        height: 80vh;
        padding-top: 10vh;
        display: flex;
        justify-content: space-around;
        overflow: auto;
        filter: blur(0px);
        pointer-events: all;
        transition: all 1s ease;

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
        transition: all 1s ease;

    }

    .interfaz-eliminar{

        width: 100%;
        height: 85vh;
        display: flex;
        justify-content: center;
        align-items: center;
        position: absolute;
        box-sizing: border-box;
        padding: 2%;
        overflow: hidden;

    }
    
    @keyframes mensajeCreado{

        0%{

            transform: translateY(-800px);

        }

        50%{

            transform: translateY(50px);

        }

        100%{

            transform: translateY(0);

        }

    }

    .messages-enter-active, .messages-leave-active {
        animation: mensajeCreado 1s ease;
    }

    .messages-enter-from, .messages-leave-to {
        animation: mensajeCreado 1s ease reverse;
    }

</style>