<template>
    <section class="services-all">
        
        <article class="services-all-srv" v-for="(service, i) in pinia.listaServicios" :key="i">

            <div class="services-all-srv-img">

                <img :src="service.img" alt="">

            </div>

            <div class="services-all-srv-data">

                <h1> {{ service.nombre }} </h1>
                <p> <strong> Descripcion:  </strong> {{ service.descripcion }} </p>
                <p> <strong> Precio:  </strong> {{ service.precio }} </p>

            </div>

        </article>

    </section>
</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia';

    const pinia = useStore()

</script>

<style lang="scss" scoped>

    .services-all{

        width: 100%;
        height: 85vh;
        overflow: auto;
        margin-top: 5vh;
        display: flex;
        flex-direction: column;
        align-items: center;

        &-srv{

            width: 60%;
            height: max-content;
            box-sizing: border-box;
            padding: 5%;
            display: flex;
            justify-content: space-between;

            &-img{

                width: 20%;

            }

            &-data{

                width: 70%;
                height: 100%;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: space-between;

                h1{

                    font-size: 30px;

                }

                p{

                    align-self: flex-start;
                    font-size: 18px;

                }

            }

        }

    }

</style>