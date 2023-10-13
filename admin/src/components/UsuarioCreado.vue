<template>

    <div class="mensaje-creado">
        
        <div class="mensaje-creado-icono">
            <v-icon name="bi-check" scale="5"></v-icon>
        </div>
        <div class="mensaje-creado-texto">
            <p> El usuario fue creado exitosamente </p>
        </div>

    </div>
</template>

<script setup>

    import { useStore } from '@/store/pinia'

    const pinia = useStore()

    setTimeout(() => {

        pinia.mensajeUsuarioRegistrado = false

    }, 3500)

</script>

<style lang="scss" scoped>

    .mensaje-creado{

        width: 20%;
        height: 10%;
        position: absolute;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 15px;
        position: absolute;
        z-index: 1000000;
        background: $first-color;
        color: #fff;
        border-radius: 15px;

        &-icono{

            height: 100%;
            width: 20%;
            display: flex;
            justify-content: center;
            align-items: center;

        }

        &-texto{

            width: 75%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;


        }

    }

</style>
