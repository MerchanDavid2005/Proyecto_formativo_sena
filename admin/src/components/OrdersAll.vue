<template>

    <div class="orders-all">
        
        <section class="orders-all-table">
            <div class="orders-all-table-title">
                <div>
                    <strong> Usuario </strong>
                </div>
                <div>
                    <strong> Lista productos </strong>
                </div>
                <div>
                    <strong> Fecha </strong>
                </div>
                <div>
                    <strong> Eliminar </strong>
                </div>
            </div>
            <transition-group name="newOrder" tag="article">
                <h1 v-if="pinia.listaPedidosFilter < 1"> No hay resultados de tu busqueda </h1>
                <div class="orders-all-table-data" v-for="(order, i) in pinia.listaPedidosFilter" :key="i">
                    <div>
                        <p> {{ order.nombre }} </p>
                    </div>
                    <div>
                        <span v-for="(prd, i) in order.lista_productos" :key="i">
                            {{ prd.nombre }},    
                        </span>
                    </div>
                    <div>
                        <p> {{ order.fecha.slice(0, 10) }} / {{ order.fecha.slice(11, 16) }} </p>
                    </div>
                    <div style="color: #f05;">
                        <v-icon 
                            @click="emits('eliminar'); pinia.idEliminar = order.id"
                            style="cursor:pointer" 
                            name="ri-delete-back-2-fill" 
                            scale="2">
                        </v-icon>
                    </div>
                </div>
            </transition-group>
        </section>

    </div>

</template>

<script setup>

    import { useStore } from '@/store/pinia';
    import { defineEmits } from 'vue'

    const emits = defineEmits(['eliminar'])
    const pinia = useStore()

</script>

<style lang="scss" scoped>

    .orders-all{

        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;

        &-table{

            width: 100%;
            height: max-content;
            display: flex;
            flex-direction: column;

            &-title{

                width: 100%;
                height: max-content;
                display: flex;
                justify-content: space-evenly;
                margin-bottom: 15px;

                div{

                    width: 20%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 5px;

                }

                div:nth-child(2){

                    width: 40%;
                    overflow: auto;

                }

            }

            article{

                width: 100%;
                display: flex;
                flex-direction: column-reverse;

                h1{

                    text-align: center;

                }

                .orders-all-table-data{

                    width: 100%;
                    height: max-content;
                    display: flex;
                    justify-content: space-evenly;
                    
                    div{
    
                        width: 20%;
                        height: 100px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        padding: 5px;
    
                    }
    
                    div:nth-child(2){
    
                        width: 40%;
                        overflow: auto;
    
                    }
    
                }

            }   

        }

    }

    .newOrder-move, .newOrder-enter-active, .newOrder-leave-active{

        transition: all 1s ease-in-out;

    }

    .newOrder-enter-from, .newOrder-leave-to{

        transform: translateX(-80px);
        opacity: 0;

    }

    .newOrder-leave-active{

        position: absolute;

    }

</style>