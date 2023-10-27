<template>

    <MainDefault>

        <div class="cuerpo-login">

            <div class="cuerpo-login-fondo"></div>

            <div class="cuerpo-login-content">

                <LoginComp />

            </div>

            <div class="cuerpo-login-mensaje">

                <transition name="panelMensaje">
                
                    <UserCreated v-show="pinia.mensajeUsuarioRegistrado" />

                </transition>

            </div>

        </div>

    </MainDefault>

</template>

<script lang="ts" setup>

    import MainDefault from '../layouts/MainDefault.vue';
    import LoginComp from '../components/LoginComp.vue';
    import UserCreated from '../components/UserCreated.vue';

    import { useStore } from '../store/pinia';

    const pinia = useStore()

</script>

<style lang="scss" scoped>

    .cuerpo-login{

        width: 100%;
        height: 90vh;
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

        &-fondo{

            width: 100%;
            height: 90vh;
            background: url(https://www.lavanguardia.com/andro4all/hero/2021/01/aplicaciones-aprender-mecanica.jpg?width=768&aspect_ratio=16:9&format=nowebp);
            background-size: 100%;
            background-repeat: no-repeat;
            filter: blur(4px);
            position: absolute;
            z-index: 1;

        }

        &-mensaje{

            width: 100%;
            height: 90vh;
            display: flex;
            justify-content: flex-end;
            align-items: flex-start;
            padding: 2%;
            box-sizing: border-box;
            position: absolute;
            z-index: 10;
            overflow: hidden;

        }

    }

    @keyframes mensajeCreado{

        0%{

            transform: translateX(300px);

        }

        50%{

            transform: translateX(-50px);

        }

        100%{

            transform: translateX(0);

        }

    }

    .panelMensaje-enter-active{

        animation: mensajeCreado 1s;

    }

    .panelMensaje-leave-active{

        animation: mensajeCreado 1s reverse;

    }


</style>