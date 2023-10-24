<template>
    <div class="car-all">

        <p v-if="!pinia.usuarioLogeado && pinia.carrito.length > 0" class="mensaje-iniciar-sesion"> Para realizar un pedido primero debes iniciar sesion </p>

        <div class="car-all-none" v-if="pinia.carrito.length < 1">

            <v-icon name="bi-cart-x-fill" scale="5"> </v-icon>
            <h1> Carrito vacio </h1>
            <p> Aun no tienes ningun producto añadido a tu carrito de compras </p>
            <button @click="enrutado.push('/')"> Añadir productos </button>

        </div>
        
        <button 
            v-if="pinia.carrito.length > 0 && pinia.usuarioLogeado" 
            @click="limpiarCarrito" 
            class="car-all-pedido"> 
            Realizar pedido 
            <v-icon style="margin-left:5px;" name="bi-check-circle-fill" scale="1"></v-icon>
        </button>

        <button 
            v-if="pinia.carrito.length > 0 && !pinia.usuarioLogeado" 
            @click="enrutado.push('/iniciar_sesion')" 
            class="car-all-pedido"> 
            Iniciar sesion
            <v-icon style="margin-left:5px;" name="hi-login" scale="1"></v-icon>
        </button>
        
        <div class="car-all-prd" v-for="(prd, i) in pinia.carrito" :key="i">

            <h1> {{ prd.nombre }} </h1>
            <p> <strong> Categoria:  </strong> {{ prd.categoria }} </p>
            <div class="car-all-prd-img">
                <img :src="prd.img" :alt="prd.nombre">
            </div>
            <p class="car-all-prd-descripcion"> <strong> Descripcion:  </strong> {{ prd.descripcion }} </p>
            <p> <strong> Cantidad:  </strong> {{ prd.cantidad }} </p>
            <p> <strong> Precio:  </strong> {{ prd.precio }} </p>
            <button @click="eliminar(i)"> 
                Eliminar del carrito 
                <v-icon name="bi-cart-x-fill" scale="1.3"></v-icon>
            </button>

        </div>

    </div>
</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia'
    import { useRouter } from 'vue-router';
    import { defineEmits, defineAsyncComponent } from 'vue';

    const mensajeEliminar = defineAsyncComponent(() => import('./VerifyDelete.vue'))
    const mensajeComprado = defineAsyncComponent(() => import('./OrderExit.vue'))

    const enrutado = useRouter()
    const pinia = useStore()
    const emits = defineEmits(['eliminar'])

    const eliminar = (id: number) => {

        emits('eliminar', mensajeEliminar)

        pinia.idEliminar = id

    }

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

        pinia.carrito = []
        localStorage.removeItem("Carrito")
        emits('eliminar', mensajeComprado)
        pinia.getPedidos()

    }

</script>

<style lang="scss" scoped>

    .car-all{

        width: 95%;
        padding-top: 5vh;
        height: max-content;
        box-sizing: border-box;
        display: flex;
        justify-content: space-evenly;
        flex-wrap: wrap;

        .mensaje-iniciar-sesion{

            position: fixed;
            top: 5%;
            font-size: 20px;

        }

        .car-all-pedido{

            position: fixed;
            left: 2%;
            top: 5%;
            @include botones($fondo-boton-crear);
            height: max-content;
            display: flex;
            align-items: center;
            z-index: 1000;

        }

        &-none{

            width: 30%;
            height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: space-evenly;
            align-items: center;
            padding: 20px;
            border-radius: 30px;
            background: $fondo-input;
            color: #000;
        
            button{

                @include botones('#0af');

            }

        }

        &-prd{

            width: 30%;
            height: 500px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            margin: 20px 0;
            transition: transform 0.5s ease-in-out;

            h1{

                text-align: center;
                margin-bottom: 20px;

            }

            &-img{

                width: 100%;
                height: 30%;
                margin: 10px 0;

            }

            p{

                margin: 10px 0;
                font-size: 15px;

            }

            &-descripcion{

                height: 15%;
                overflow: auto;

            }

            button{

                @include botones($fondo-boton-eliminar);
                align-self: center;
                width: 55%;
                font-size: 15px;
                padding: 10px;
                margin-top: 10px;

            }

        }

        &-prd:hover{

            transform: scale(1.05);

        }
    
    }

</style>