<template>

    <div class="verify-buy">
        
        <h1> Realizar pedido </h1>
        <p> ¿Estas seguro de querer realizar el pedido? </p>
        <div class="verify-buy-buttons">
            <button @click="limpiarCarrito"> Si, seguro </button>
            <button @click="emits('ocultar')"> No, Cancelar </button>
        </div>

    </div>

</template>

<script lang="ts" setup>

    import { defineEmits } from 'vue';
    import { useStore } from '../store/pinia';

    const pinia = useStore()
    const emits = defineEmits(['ocultar', 'mostrarMensaje'])

    async function hacerPedido(){

        const data = await fetch("http://localhost:8000/api/Pedido/", {

            method: 'POST',
            body: JSON.stringify({

                pedido_usuario: pinia.datosUsuario.id,
                lista_productos: JSON.stringify(pinia.carrito)

            }),
            headers: {"content-type" : "application/json"}

        })

        return data

    }

    async function generarPdf(){

        await hacerPedido()

        let carrito = new FormData()

        carrito.append("id", `${pinia.listaPedidos.length + 1}`)
        carrito.append("usuario", pinia.datosUsuario.nombre_usuario)
        carrito.append("nombre", pinia.datosUsuario.nombre)
        carrito.append("correo", pinia.datosUsuario.email)
        carrito.append("carrito", JSON.stringify(pinia.carrito))

        const data = await fetch(`http://localhost:8000/generate/factur/`, {

            method: 'POST',
            body: carrito

        })

        return data.json

    }

    async function limpiarCarrito() {

        await generarPdf()

        fetch("http://localhost:8000/send/factur/", {

            method: 'POST',
            body: JSON.stringify({

                id: pinia.listaPedidos.length + 1,
                usuario: pinia.datosUsuario.nombre_usuario,
                email: pinia.datosUsuario.email

            }),
            headers: {"content-type": "application/json"}

        })

        emits('ocultar')
        pinia.getPedidos()

        setTimeout(() => {

            pinia.carrito = []
            localStorage.removeItem("Carrito")

        }, 1000)

        setTimeout(() => {

            emits('mostrarMensaje')

        }, 1500)

        setTimeout(() => {

            emits('mostrarMensaje')

        }, 4000)

    }

</script>

<style lang="scss" scoped>

    .verify-buy{

        width: max-content;
        height: max-content;
        padding: 15px 50px;
        border-radius: 15px;
        background: $fondo-boton-crear;
        color: #fff;
        position: absolute;
        z-index: 1000000;

        h1, p{

            margin: 10px 0;

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