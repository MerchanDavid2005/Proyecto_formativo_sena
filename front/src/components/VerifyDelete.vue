<template>
    <div class="verify-delete">
        
        <h1> Eliminar </h1>
        <p> ¿Estas seguro de querer eliminar este producto del carrito? </p>
        <div class="verify-delete-buttons">
            <button @click="actualizar"> Si, seguro </button>
            <button @click="emits('ocultar')"> No, Cancelar </button>
        </div>

    </div>
</template>

<script lang="ts" setup>

    import { defineEmits } from 'vue';
    import { useStore } from '../store/pinia'

    const pinia = useStore()
    const emits = defineEmits(['ocultar'])

    const aceptado = async () => {

        pinia.datosUsuario.carrito.splice(pinia.idEliminar, 1)
        
        const data = await fetch(`http://localhost:8000/get/user/${pinia.datosUsuario.id}/`, {

            method: 'POST',
            body: JSON.stringify({

                carrito: pinia.datosUsuario.carrito

            }),
            headers: {"content-type": "application/json"}

        })

        return data.json()

    }

    const actualizar = async () => {

        emits('ocultar')
        await aceptado()
        pinia.getUsuario(pinia.datosUsuario.id)

    }

</script>

<style lang="scss" scoped>

    .verify-delete{

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
                font-weight: lighter;

            }

            button:nth-child(2){

                @include botones('#fff');
                margin-top: 20px;
                color: #000;
                font-weight: lighter;

            }

        }

    }

</style>