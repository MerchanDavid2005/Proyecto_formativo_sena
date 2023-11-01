<template>

    <div class="login">

        <div class="login-fondo"></div>

        <div :class="{'login-body': !pinia.cargandoDatos, 'login-body-none': pinia.cargandoDatos}">

            <LoginComp />

        </div>

        <div class="login-mensaje">

            <transition name="panelMensaje">
            
                <UsuarioCreado v-show="pinia.mensajeUsuarioRegistrado" />

            </transition>

            <transition name="panelMensaje">
            
                <MessagesSesion v-show="pinia.messagesSesionCaducada" />

            </transition>

            <transition name="panelMensaje">

                <MessagesError v-show="pinia.errorFetch" />

            </transition>

        </div>

        <div class="login-load">

            <LoaderCompVue v-show="pinia.cargandoDatos" />

        </div>

    </div>

</template>

<script setup>

    import LoginComp from '@/components/LoginComp.vue';
    import UsuarioCreado from '@/components/UsuarioCreado.vue';
    import MessagesSesion from '@/components/MessagesSesion.vue';
    import MessagesError from '@/components/MessagesError.vue';
    import LoaderCompVue from '../components/LoaderComp.vue';

    import { useStore } from '@/store/pinia';

    const pinia = useStore()
    
</script>

<style lang="scss" scoped>

    .login{

        width: 100%;
        height: 100vh;
        display: flex;
        overflow: hidden;

        &-fondo{

            width: 100%;
            height: 100vh;
            position: absolute;
            background: url(https://laadministracionelectronica.files.wordpress.com/2014/10/fondo1.jpg);
            filter: blur(4px);
            background-repeat: no-repeat;
            background-size: 100%;
            overflow: hidden;

        }

        &-body{

            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            position: static;
            z-index: 10;
            overflow: hidden;

        }

        &-body-none{

            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            position: static;
            z-index: 10;
            overflow: hidden;
            background: #444;
            filter: brightness(20%);

        }

        &-mensaje{

            width: 100%;
            height: 100vh;
            display: flex;
            justify-content: flex-end;
            align-items: flex-start;
            padding: 2%;
            position: absolute;
            overflow: hidden;

        }

        &-load{

            width: 100%;
            height: 100vh;
            display: flex;
            position: absolute;

        }

    }

    @keyframes mensajeCreado{

        0%{

            transform: translateX(600px);

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