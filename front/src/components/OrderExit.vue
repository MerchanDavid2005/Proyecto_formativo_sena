<template>

    <div class="messages-exit">

        <h1> ¡Pedido realizado! </h1>
        <p> El pedido se ha hecho correctamente, gracias por tu compra :) </p>
        <button @click="emits('ocultar')"> Aceptar </button>

    </div>

</template>

<script lang="ts" setup>

    import { defineEmits } from 'vue';

    const emits = defineEmits(['ocultar'])

</script>

<style lang="scss" scoped>

    .messages-exit{

        width: max-content;
        height: max-content;
        padding: 15px 50px;
        border-radius: 15px;
        background: $fondo-boton-crear;
        color: #fff;
        position: absolute;
        z-index: 1000;

        h1, p{

            margin: 10px 0;

        }

        button{

            @include botones(#fff);
            color: #000;
            font-weight: lighter;

        }

    }

</style>