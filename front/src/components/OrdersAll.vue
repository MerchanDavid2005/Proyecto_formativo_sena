<template>

    <div class="orders-all">

        <h1 class="orders-all-titulo" v-if="pinia.listaPedidos.length < 1"> Aun no has realizado ningun pedido </h1>
        <h1 class="orders-all-titulo" v-if="pinia.listaPedidos.length > 0"> Pedidos que has realizado </h1>

        <div class="orders-all-productos">

            <div class="orders-all-productos-prd" v-for="(order, i) in pinia.listaPedidos" :key="i">
                <div class="orders-all-productos-prd-img">
                    <div 
                        :class="{'img-1': order.lista_productos.length == 1}"
                        v-for="(prd, i) in order.lista_productos.slice(0, 4) " :key="i">
                        <img :src="prd.img" alt="">
                    </div>
                </div>
                <p> <strong> Fecha:  </strong> {{ order.fecha }} </p>
                <button @click="informacionPedido(order.id)">
                    Ver informacion del pedido
                </button>
            </div>

        </div>
        
    </div>

</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia';
    import { useRouter } from 'vue-router';

    const router = useRouter()
    const pinia = useStore()

    const informacionPedido = (id: number) => router.push(`/pedido/${id}`)

</script>

<style lang="scss" scoped>

    .orders-all{

        width: 100%;
        height: 20%;
        display: flex;
        flex-direction: column;
        align-items: center;

        &-titulo{

            margin-bottom: 10vh;

        }

        &-productos{

            width: 100%;
            height: max-content;
            display: flex;
            justify-content: space-evenly;
            flex-wrap: wrap;

            &-prd{

                width: 30%;
                height: 400px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                align-items: center;
                transition: transform 0.5s ease-in-out;
                margin: 20px 0;
    
                &-img{
    
                    width: 100%;
                    height: 70%;
                    display: grid;
                    grid-template-columns: repeat(2, 20%);
                    gap: 5px;
                    justify-content: center;

                    img{

                        object-fit: contain;

                    }
                    .img-1{

                        grid-column: 1 / 3;
                        grid-row: 1 / 3;

                    }
    
                }

                p{

                    margin: 10px 0

                }

                button{

                    @include botones($fondo-boton-crear);
                    margin: 10px 0;

                }
    
            }

            &-prd:hover{

                transform: scale(1.05);

            }
    
        }

    }

    @media(min-width: 1600px){

        .orders-all-productos-prd-img{

            height: 80%;

        }

    }

</style>