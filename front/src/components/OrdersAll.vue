<template>

    <div class="orders-all">

        <h1 v-if="pinia.listaPedidos.length < 1"> Aun no has realizado ningun pedido </h1>

        <div class="orders-all-prd" v-for="(order, i) in pinia.listaPedidos" :key="i">
            <h1> Numero de pedido: {{ i + 1 }} </h1>
            <div class="orders-all-prd-img">
                <div v-for="(prd, i) in order.lista_productos.slice(0, 4) " :key="i">
                    <img :src="prd.img" alt="">
                </div>
            </div>
            <p> <strong> Fecha:  </strong> {{ order.fecha }} </p>
            <router-link :to="{name: 'pedido', params: {id: order.id}}">
                Ver informacion del pedido
            </router-link>
        </div>
        
    </div>

</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia';

    const pinia = useStore()

</script>

<style lang="scss" scoped>

    .orders-all{

        width: 100%;
        height: 85vh;
        padding-top: 5vh;
        overflow: auto;
        display: flex;
        justify-content: space-evenly;
        flex-wrap: wrap;

        &-prd{

            width: 30%;
            height: 600px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;

            &-img{

                width: 100%;
                height: 80%;
                display: grid;
                grid-template-columns: repeat(2, 130px);
                gap: 15px;
                justify-content: center;

                div{

                    width: 100%;
                    height: 100%;

                    img{

                        object-fit: cover;

                    }

                }

            }

        }

    }

</style>