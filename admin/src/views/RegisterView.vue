<template>
    <div class="register">

        <div class="register-fondo"></div>
        
        <RegisterComp />

    </div>
</template>

<script setup>

    import RegisterComp from '@/components/RegisterComp.vue';

</script>

<style lang="scss" scoped>

    .register{

        width: 100%;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        position: static;
        z-index: 10;

        &-fondo{

            width: 100%;
            height: 100vh;
            position: absolute;
            background: url(https://laadministracionelectronica.files.wordpress.com/2014/10/fondo1.jpg);
            filter: blur(4px);
            background-repeat: no-repeat;
            background-size: 100%;

        }

    }

</style>