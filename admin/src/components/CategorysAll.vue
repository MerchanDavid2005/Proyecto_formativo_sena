<template>

    <div class="categorys-all">
        
        <section class="categorys-all-table">
            <div class="categorys-all-table-title">
                <div>
                    <strong> Nombre </strong>
                </div>
                <div>
                    <strong> Actualizar </strong>
                </div>
                <div>
                    <strong> Eliminar </strong>
                </div>
            </div>
            <transition-group name="newCategory" tag="article">
                <div class="categorys-all-table-data" v-for="(cate, i) in pinia.listaCategoriasFilter" :key="i">
                    <div>
                        <p> {{ cate.nombre }} </p>
                    </div>
                    <div style="color: #0fa;">
                        <v-icon 
                            @click="enrutado.push(`/admin/edit/category/${i}`)"
                            style="cursor:pointer" 
                            name="md-modeeditoutline" 
                            scale="2">
                        </v-icon> 
                    </div>
                    <div style="color: #f05;">
                        <v-icon 
                            @click="emits('eliminar'); pinia.idEliminar = cate.id"
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
    import { useRouter } from 'vue-router';

    const emits = defineEmits(['eliminar'])
    const pinia = useStore()
    const enrutado = useRouter()

</script>

<style lang="scss" scoped>

    .categorys-all{

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

                    width: 30%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 5px;

                }

            }

            article{

                width: 100%;
                display: flex;
                flex-direction: column-reverse;

                .categorys-all-table-data{

                    width: 100%;
                    height: max-content;
                    display: flex;
                    justify-content: space-evenly;
                    
                    div{
    
                        width: 30%;
                        height: 100px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        padding: 5px;
    
                    }
    
                }

            }   

        }

    }

    .newCategory-enter-active, .newCategory-leave-active{

        transition: all 1s ease-in-out;

    }

    .newCategory-enter-from, .newCategory-leave-to{

        transform: translateX(-80px);
        opacity: 0;

    }

</style>