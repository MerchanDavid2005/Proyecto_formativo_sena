<template>

    <div class="cuerpo-register">

        <div :class="{'cuerpo-register-fondo': !panelCodigo, 'cuerpo-register-fondo-none': panelCodigo}"></div>

        <div :class="{'cuerpo-register-content': !panelCodigo, 'cuerpo-register-content-none': panelCodigo}">

            <RegisterComp @verificar="verificarUsuario" />

        </div>

        <div class="cuerpo-register-verify">

            <button v-show="panelCodigo" @click="verificarUsuario" class="cuerpo-register-verify-cancel"> Cancelar </button>

            <transition name="transitionVerify">
            
                <CodeVerify v-show="panelCodigo" />

            </transition>

        </div>

    </div>

</template>

<script lang="ts" setup>

    import RegisterComp from '../components/RegisterComp.vue';
    import CodeVerify from '../components/CodeVerify.vue';

    import { ref } from 'vue';

    let panelCodigo = ref<boolean>(false)

    const verificarUsuario = () => panelCodigo.value = !panelCodigo.value

</script>

<style lang="scss" scoped>

    .cuerpo-register{

        width: 100%;
        height: 100vh;
        display: flex;

        &-content{

            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            position: static;
            z-index: 50;

        }

        &-content-none{

            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            position: static;
            z-index: 50;
            filter: brightness(20%);
            pointer-events: none;

        }

        &-fondo{

            width: 100%;
            height: 100%;
            background: url(https://www.lavanguardia.com/andro4all/hero/2021/01/aplicaciones-aprender-mecanica.jpg?width=768&aspect_ratio=16:9&format=nowebp);
            background-size: 100%;
            background-repeat: no-repeat;
            filter: blur(4px);
            position: absolute;
            z-index: 1;

        }

        &-fondo-none{

            width: 100%;
            height: 100%;
            background: url(https://www.lavanguardia.com/andro4all/hero/2021/01/aplicaciones-aprender-mecanica.jpg?width=768&aspect_ratio=16:9&format=nowebp);
            background-size: 100%;
            background-repeat: no-repeat;
            filter: blur(4px) brightness(20%);
            position: absolute;
            z-index: 1;

        }

        &-verify{

            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            position: absolute;

            &-cancel{

                position: absolute;
                right: 2%;
                top: 5%;
                z-index: 1000;
                @include botones($fondo-boton-limpiar);

            }

        }

    }

    .transitionVerify-enter-active, .transitionVerify-leave-active{

        transition: transform 0.5s ease;

    }

    .transitionVerify-enter-from, .transitionVerify-leave-to{

        transform: scale(0);

    }

</style>