<template>
    <div class="car-all">

        <h1 
            v-if="pinia.carritoFiltrar.length < 1 && pinia.carrito.length > 1"> 
            No tienes productos por esta categoria 
        </h1>

        <h1 v-if="pinia.carrito.length < 1"> No tienes productos en el carrito </h1>
        
        <button 
            v-if="pinia.carrito.length > 0" 
            @click="hacerPedido" 
            class="car-all-pedido"> 
            Realizar pedido 
        </button>
        
        <div class="car-all-prd" v-for="(prd, i) in pinia.carritoFiltrar" :key="i">

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
    import { defineEmits } from 'vue';

    const pinia = useStore()
    const emits = defineEmits(['eliminar'])

    const eliminar = (id: number) => {

        emits('eliminar')

        pinia.idEliminar = id

    }

    function hacerPedido(){

        fetch("http://localhost:8000/api/Pedido/", {

            method: 'POST',
            body: JSON.stringify({

                pedido_usuario: 1,
                lista_productos: JSON.stringify(pinia.carrito)

            }),
            headers: {"content-type" : "application/json"}

        })

        pinia.carrito = []
        pinia.carritoFiltrar = []
        localStorage.removeItem("Carrito")

        setTimeout(() => {

            pinia.getPedidos()

        })

    }

</script>

<style lang="scss" scoped>

    .car-all{

        width: 80%;
        height: max-content;
        box-sizing: border-box;
        display: flex;
        justify-content: space-evenly;
        flex-wrap: wrap;

        .car-all-pedido{

            position: sticky;
            top: 0;
            @include botones($fondo-boton-crear);
            height: max-content;

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
                font-size: 18px;

            }

            &-descripcion{

                height: 15%;
                overflow: auto;

            }

            button{

                @include botones($fondo-boton-eliminar);
                align-self: center;
                width: 65%;
                font-size: 18px;
                padding: 15px;
                margin-top: 10px;

            }

        }

        &-prd:hover{

            transform: scale(1.05);

        }
    
    }

</style>