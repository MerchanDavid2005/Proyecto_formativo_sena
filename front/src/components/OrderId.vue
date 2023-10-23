<template>

    <div class="order-id">

        <button @click="enrutado.push('/perfil')" class="order-id-volver">
            <v-icon style="margin-right:5px;" name="bi-arrow-left-short" scale="1.5"></v-icon>
            Volver
        </button>

        <div class="order-id-data" v-for="(prd, i) in pinia.idPedido.lista_productos" :key="i">

            <h1> {{ prd.nombre }} </h1>
            <p> <strong> Categoria:  </strong> {{ prd.categoria }} </p>
            <div class="order-id-data-img">
                <img :src="prd.img" :alt="prd.nombre">
            </div>
            <p class="order-id-data-descripcion"> <strong> Descripcion:  </strong> {{ prd.descripcion }} </p>
            <p> <strong> Cantidad:  </strong> {{ prd.cantidad }} </p>
            <p> <strong> Precio:  </strong> {{ prd.precio }} </p>

        </div>

    </div>

</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia';
    import { useRoute, useRouter } from 'vue-router';
    import { onMounted } from 'vue'

    const enrutado = useRouter()
    const pinia = useStore()
    const router = useRoute()

    onMounted(() => {

        pinia.getPedidoId(router.params.id)

    })

</script>

<style lang="scss" scoped>

    .order-id{

        width: 100%;
        height: 85vh;
        padding: 5vh;
        box-sizing: border-box;
        overflow: auto;
        display: flex;
        justify-content: space-evenly;
        flex-wrap: wrap;

        &-volver{

            position: fixed;
            left: 2%;
            top: 15%;
            @include botones($fondo-boton-limpiar);
            height: max-content;
            display: flex;
            align-items: center;
            z-index: 1000;

        }

        &-data{

            width: 30%;
            height: 500px;
            display: flex;
            flex-direction: column;
            box-sizing: border-box;
            display: flex;
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

        }

        &-data:hover{

            transform: scale(1.05);

        }

    }

</style>