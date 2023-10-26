<template>

    <div class="login">

        <div class="login-fondo"></div>

        <div class="login-body">

            <LoginComp />

        </div>

        <div class="login-mensaje">

            <transition name="panelMensaje">
            
                <UsuarioCreado v-show="pinia.mensajeUsuarioRegistrado" />

            </transition>

            <transition name="panelMensaje">
            
                <MessagesSesion v-show="pinia.messagesSesionCaducada" />

            </transition>

        </div>

    </div>

</template>

<script setup>

    import LoginComp from '@/components/LoginComp.vue';
    import UsuarioCreado from '@/components/UsuarioCreado.vue';
    import MessagesSesion from '@/components/MessagesSesion.vue';

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