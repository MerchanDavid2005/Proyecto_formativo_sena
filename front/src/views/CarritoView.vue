<template>
    <MainDefault>

        <div class="interfaz-panel">

            <transition name="verifyPanel">

                <VerifyDelete v-show="mensajeEliminar" @ocultar="ocultarMensaje" />

            </transition>

            <transition name="verifyPanel">

                <OrderVerify v-show="mensajeAceptar" @ocultar="ocultarMensaje" @mostrarMensaje="mostrarMensajeComprado" />

            </transition>

            <transition name="messagges">

                <MessagesExit v-show="mensajeComprado" />
            
            </transition>

        </div>

        <main :class="
            {'cuerpo-carrito-view': !mensajeEliminar || !mensajeAceptar,
            'cuerpo-none' : mensajeEliminar || mensajeAceptar}">

            <CarAll @eliminar="mostrarMensaje"/>

        </main>

    </MainDefault>
</template>

<script lang="ts" setup>

    import MainDefault from '../layouts/MainDefault.vue';
    import CarAll from '../components/CarAll.vue';
    import VerifyDelete from '../components/VerifyDelete.vue';
    import OrderVerify from '../components/OrderVerify.vue';
    import MessagesExit from '../components/MessagesExit.vue';

    import { ref } from 'vue';

    let mensajeComprado = ref<boolean>(false)

    let mensajeEliminar = ref<boolean>(false)
    let mensajeAceptar = ref<boolean>(false)

    const mostrarMensaje = (mensaje: string) => {

        if(mensaje == "Eliminar"){

            mensajeEliminar.value = true
            mensajeAceptar.value = false

        }else{

            mensajeEliminar.value = false
            mensajeAceptar.value = true

        }

    }

    const ocultarMensaje = () => { 
        
        mensajeEliminar.value = false
        mensajeAceptar.value = false

    }

    const mostrarMensajeComprado = () => mensajeComprado.value = !mensajeComprado.value

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

    .interfaz-panel{

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
    

    .verifyPanel-enter-active, .verifyPanel-leave-active {
        
        transition: transform 1s ease-in-out;

    }

    .verifyPanel-enter-from, .verifyPanel-leave-to {

        transform: scale(0);

    }

    @keyframes mensaje {

        0%{

            transform: translateX(600px);

        }

        50%{

            transform: translateX(-50px);

        }

        100%{

            transform: translateX(0px)

        }
        
    }

    .messagges-enter-active {
        
        animation: mensaje 1s;

    }

    .messagges-leave-active {

        
        animation: mensaje 1s reverse;

    }
</style>