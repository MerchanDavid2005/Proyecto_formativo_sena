<template>

    <div class="messages-buy">
        
        <h1> Pedido realizado </h1>
        <p> El pedido fue realizado exitosamente </p>

    </div>

</template>

<script lang="ts" setup>

    import { defineEmits } from 'vue';

    const emits = defineEmits(['mostrarMensaje'])

</script>

<style lang="scss" scoped>

    .messages-buy{

        width: 30%;
        height: max-content;
        padding: 15px;
        border-radius: 20px;
        background: $fondo-boton-crear;
        color: #fff;
        align-self: flex-start;
        justify-self: flex-end;
        z-index: 100000;

    }

</style>