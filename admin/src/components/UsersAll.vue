<template>

    <div class="users-all">
        
        <section class="users-all-table">
            <div class="users-all-table-title">
                <div>
                    <strong> Usuario </strong>
                </div>
                <div>
                    <strong> Nombre </strong>
                </div>
                <div>
                    <strong> Foto </strong>
                </div>
                <div>
                    <strong> Email </strong> 
                </div>
                <div>
                    <strong> Rol </strong> 
                </div>
                <div>
                    <strong> Eliminar </strong>
                </div>
            </div>
            <transition-group name="newUser" tag="article">
                <h1 v-if="pinia.listaUsuariosFilter < 1"> No hay resultados de tu busqueda </h1>
                <div class="users-all-table-data" v-for="(user, i) in pinia.listaUsuariosFilter" :key="i">
                    <div v-show="pinia.datosUsuarioIngresado.id != user.id">
                        <p> {{ user.nombre_usuario }} </p>
                    </div>
                    <div v-show="pinia.datosUsuarioIngresado.id != user.id">
                        <p> {{ user.nombre }} </p>
                    </div>
                    <div v-show="pinia.datosUsuarioIngresado.id != user.id">
                        <img :src="user.foto" :alt="user.nombre">
                    </div>
                    <div v-show="pinia.datosUsuarioIngresado.id != user.id">
                        <p> {{ user.email }} </p>
                    </div>
                    <div v-show="pinia.datosUsuarioIngresado.id != user.id">
                        <p> {{ user.rol }} </p>
                    </div>
                    <div v-show="pinia.datosUsuarioIngresado.id != user.id" style="color: #f05;">
                        <v-icon 
                            @click="emits('eliminar'); pinia.idEliminar = user.id"
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

    .users-all{

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

                h1{

                    text-align: center;

                }

                .users-all-table-data{

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

    @media(max-width:1300px){

        .users-all{

            font-size: 13px;
            
        }

    }

    .newUser-move, .newUser-enter-active, .newUser-leave-active{

        transition: all 1s ease-in-out;

    }

    .newUser-enter-from, .newUser-leave-to{

        transform: translateX(-80px);
        opacity: 0;

    }

    .newUser-leave-active{

        position: absolute;

    }

</style>