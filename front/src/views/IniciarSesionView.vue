<template>

    <div class="cuerpo-login">

        <div class="cuerpo-login-fondo"></div>

        <div class="cuerpo-login-content">

            <LoginComp />

        </div>

    </div>

</template>

<script lang="ts" setup>

    import LoginComp from '../components/LoginComp.vue';

</script>

<style lang="scss" scoped>

    .cuerpo-login{

        width: 100%;
        height: 100vh;

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
            height: 100%;
            background: url(https://laadministracionelectronica.files.wordpress.com/2014/10/fondo1.jpg);
            background-size: 100%;
            background-repeat: no-repeat;
            filter: blur(4px);
            position: absolute;
            z-index: 1;

        }

    }

</style>