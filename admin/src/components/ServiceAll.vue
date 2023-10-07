<template>

    <div class="services-all">
        
        <section class="services-all-table">
            <div class="services-all-table-title">
                <div>
                    <strong> Nombre </strong>
                </div>
                <div>
                    <strong> Foto </strong>
                </div>
                <div>
                    <strong> Descripcion </strong> 
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
            <transition-group name="newService" tag="article">
                <div class="services-all-table-data" v-for="(service, i) in pinia.listaServiciosFilter" :key="i">
                    <div>
                        <p> {{ service.nombre }} </p>
                    </div>
                    <div>
                        <img :src="service.img" :alt="service.nombre">
                    </div>
                    <div>
                        <p> {{ service.descripcion }} </p>
                    </div>
                    <div>
                        <p> {{ service.precio }} </p>
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
                            @click="emits('eliminar'); pinia.idEliminar = service.id"
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

    .services-all{

        width: 100%;
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

                    width: 15%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 5px;

                }

                div:nth-child(3){

                    width: 25%;
                    overflow: auto;

                }

            }

            article{

                width: 100%;
                display: flex;
                flex-direction: column-reverse;

                .services-all-table-data{

                    width: 100%;
                    height: max-content;
                    display: flex;
                    justify-content: space-evenly;
                    
                    div{
    
                        width: 15%;
                        height: 120px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        padding: 5px;
    
                    }
    
                    div:nth-child(3){
    
                        width: 25%;
                        overflow: auto;
    
                    }
    
                }

            }   

        }

    }

    .newService-enter-active, .newService-leave-active{

        transition: all 1s ease-in-out;

    }

    .newService-enter-from, .newService-leave-to{

        transform: translateX(-80px);
        opacity: 0;

    }

</style>