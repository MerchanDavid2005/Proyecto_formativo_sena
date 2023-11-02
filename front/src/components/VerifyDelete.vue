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
    const emits = defineEmits(['ocultar', 'error', 'successDelete'])

    const aceptado = async () => {

        let carritoCopy = pinia.datosUsuario.carrito.splice(pinia.idEliminar, 1)
        
        const data = await fetch(`http://localhost:8000/api/Usuario/${pinia.datosUsuario.id}/`, {

            method: 'PATCH',
            body: JSON.stringify({

                carrito: JSON.stringify(carritoCopy)

            }),
            headers: {"content-type": "application/json"}

        })

        return data.json()

    }

    const actualizar = async () => {

        pinia.pantallaCarga = true

        try{

            await aceptado();
            pinia.getUsuario(pinia.datosUsuario.id);
            pinia.pantallaCarga = false;
            emits('ocultar');
            setTimeout(() => {

                emits('successDelete')

            }, 500)


        }catch(e){

            pinia.pantallaCarga = false;
            emits('ocultar');
            setTimeout(() => {

                emits('error')

            }, 500)

        }   

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