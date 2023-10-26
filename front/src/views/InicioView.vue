<template>
    <MainDefault>

        <div class="verificar-compra">

            <transition name="cuadroCompra">
            
                <CheckBuy v-show="interfazVerificacion" @animacion="verAnimacion" @ocultar="ocultarInterfaz" />

            </transition>

            <transition name="animacionCompra">
            
                <AnimationBuy v-if="comprado" @ocultar="cerrarAnimacion" />

            </transition>

            <transition name="messagges">
            
                <MessagesSendContact v-show="pinia.correoContactoEnviado" />

            </transition>

            <transition name="messagges">
            
                <MessagesSesion v-show="pinia.mensajeTokenCaducado" />

            </transition>
            
        </div>

        <div :class="{'contenedor-compras' : funcionando, 'contenedor-compras-none' : !funcionando}">

            <FilterData />
            <ProductsAll @verificar="verificarCompra" />

        </div>

    </MainDefault>
</template>

<script lang="ts" setup>

    import { ref } from 'vue';
    import { useStore } from '../store/pinia';

    const pinia = useStore()

    import MainDefault from '../layouts/MainDefault.vue'
    import ProductsAll from '../components/ProductsAll.vue'
    import FilterData from '../components/FilterData.vue';
    import CheckBuy from '../components/CheckBuy.vue';
    import AnimationBuy from '../components/AnimationBuy.vue';
    import MessagesSendContact from '../components/MessagesSendContact.vue';
    import MessagesSesion from '../components/MessagesSesion.vue';

    let interfazVerificacion = ref<boolean>(false)
    let funcionando = ref<boolean>(true)
    let comprado = ref<boolean>(false)

    const verificarCompra = () => {
        
        interfazVerificacion.value = true
        funcionando.value = false

    }

    const ocultarInterfaz = () => {

        interfazVerificacion.value = false
        funcionando.value = true

    }

    const verAnimacion = () => {

        comprado.value = true

    }

    const cerrarAnimacion = () => {

        comprado.value = false

    }

</script>

<style lang="scss" scoped>

    .contenedor-compras{

        position: static;
        z-index: 1000;
        width: 100%;
        height: 85vh;
        display: flex;
        justify-content: space-around;
        padding-top: 5vh;
        overflow: auto;
        filter: blur(0px);
        pointer-events: all;

    }

    .contenedor-compras-none{

        position: static;
        z-index: 1000;
        width: 100%;
        height: 85vh;
        display: flex;
        justify-content: space-around;
        padding-top: 5vh;
        overflow: hidden;
        filter: blur(7px);
        pointer-events: none;

    }

    .verificar-compra{

        width: 100%;
        height: 90vh;
        display: flex;
        justify-content: center;
        align-items: center;
        position: absolute;
        overflow: hidden;

    }

    .cuadroCompra-enter-active, .cuadroCompra-leave-active {
        transition: transform 0.5s ease-in-out;
    }

    .cuadroCompra-enter-from, .cuadroCompra-leave-to {
        transform: scale(0);
    }

    .animacionCompra-enter-active, .animacionCompra-leave-active {
        transition: width 0.5s ease-in-out;
    }

    .animacionCompra-enter-from, .animacionCompra-leave-to {
        width: 0;
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

    .messagges-leave-active{

        animation: mensaje 1s reverse;

    }

</style>