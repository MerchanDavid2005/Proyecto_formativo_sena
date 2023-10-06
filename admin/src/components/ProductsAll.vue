<template>

    <div class="products-all">
        
        <h1 class="products-all-title"> Productos </h1>
        <section class="products-all-table">
            <div class="products-all-table-title">
                <div>
                    <strong> Nombre </strong>
                </div>
                <div>
                    <strong> Categoria </strong>
                </div>
                <div>
                    <strong> Foto </strong>
                </div>
                <div>
                    <strong> Descripcion </strong> 
                </div>
                <div>
                    <strong> Cantidad </strong>
                </div>
                <div>
                    <strong> Precio </strong>
                </div>
                <div>
                    <strong> Actualizar </strong>
                </div>
                <div>
                    <strong> Eliminar </strong>
                </div>
            </div>
            <transition-group name="newProduct" tag="article">
                <div class="products-all-table-data" v-for="(prd, i) in pinia.listaProductosFilter" :key="i">
                    <div>
                        <p> {{ prd.nombre }} </p>
                    </div>
                    <div>
                        <p> {{ prd.categoria }} </p>
                    </div>
                    <div>
                        <img :src="prd.img" :alt="prd.nombre">
                    </div>
                    <div>
                        <p> {{ prd.descripcion }} </p>
                    </div>
                    <div>
                        <p> {{ prd.cantidad }} </p>
                    </div>
                    <div>
                        <p> {{ prd.precio }} </p>
                    </div>
                    <div style="color: #0fa;">
                        <v-icon 
                            style="cursor:pointer" 
                            name="md-modeeditoutline" 
                            scale="2">
                        </v-icon> 
                    </div>
                    <div style="color: #f05;">
                        <v-icon 
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

    const pinia = useStore()

</script>

<style lang="scss" scoped>

    .products-all{

        width: 85%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;

        &-title{

            font-size: 50px;
            margin-bottom: 10vh;

        }

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

                    width: 10%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 5px;

                }

                div:nth-child(4){

                    width: 20%;
                    overflow: auto;

                }

            }

            article{

                width: 100%;
                display: flex;
                flex-direction: column-reverse;

                .products-all-table-data{

                    width: 100%;
                    height: max-content;
                    display: flex;
                    justify-content: space-evenly;
                    
                    div{
    
                        width: 10%;
                        height: 120px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        padding: 5px;
    
                    }
    
                    div:nth-child(4){
    
                        width: 20%;
                        overflow: auto;
    
                    }
    
                }

            }   

        }

    }

    .newProduct-enter-active, .newProduct-leave-active{

        transition: all 1s ease-in-out;

    }

    .newProduct-enter-from, .newProduct-leave-to{

        transform: translateX(-80px);
        opacity: 0;

    }

</style>