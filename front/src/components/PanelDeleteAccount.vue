<template>

    <div class="panel-eliminar-cuenta">
        
        <h1> Eliminar </h1>
        <p> ¿Estas seguro de querer eliminar tu cuenta? </p>
        <div class="panel-eliminar-cuenta-buttons">
            <button @click="emits('verify', 'confirmarDelete')"> Si, seguro </button>
            <button @click="emits('ocultar')"> No, Cancelar </button>
        </div>

    </div>

</template>

<script lang="ts" setup>

    import { defineEmits } from 'vue'

    const emits = defineEmits(['verify', 'ocultar'])

</script>

<style lang="scss" scoped>

    .panel-eliminar-cuenta{

        position: static;
        z-index: 5000;
        background: $fondo-boton-eliminar;
        outline: 2px solid #000;
        color: #fff;
        width: 30%;
        height: 25%;
        padding: 3%;
        border-radius: 10px;

        h1{

            margin-bottom: 20px;

        }

        p{

            font-size: 20px;

        }

        &-buttons{

            width: 100%;
            height: max-content;
            display: flex;
            
            button:nth-child(1){

                @include botones('#fff');
                margin-top: 20px;
                margin-right: 10px;
                color: #000;

            }

            button:nth-child(2){

                @include botones('#fff');
                margin-top: 20px;
                color: #000;

            }

        }

    }

</style>