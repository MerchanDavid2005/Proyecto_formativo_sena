<template>
    <section class="categoria">
        <div class="categoria-title">
            <h1> Tabla categorias </h1>
        </div>
        <div class="categoria-tabla">
            <table>
                <thead>
                    <tr>
                        <th> Nombre </th>
                        <th> Actualizar informacion </th>
                        <th> Eliminar </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(cate, i) in pinia.listaCategoriasFiltrar" :key="i">
                        <td> {{ cate.nombre }} </td>
                        <td> 
                            <router-link 
                                class="categoria-tabla-btn-actualizar" 
                                :to="{name: 'categoria', params: { id: cate.id}}">
                                <v-icon  
                                    name="md-changecircle-round" 
                                    scale="2">
                                </v-icon>  
                            </router-link>
                        </td>
                        <td 
                            class="categoria-tabla-btn-eliminar"> 
                            <v-icon 
                                @click="eliminarCategoria(cate.id)"
                                name="md-delete" 
                                scale="2">
                            </v-icon> 
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="categoria-nuevo">
            <button @click="nuevaCategoria"> Nueva categoria </button>
        </div>
    </section>
</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia';

    import { defineEmits } from 'vue';

    const pinia = useStore()

    const emits = defineEmits(['mostrarInterfaz'])

    const nuevaCategoria = () => emits('mostrarInterfaz', 'categoria')
    
    function eliminarCategoria(id: number){

        fetch(`http://127.0.0.1:8000/api/Categoria/${id}/`, {

            method: 'DELETE',
            headers: {"content-type" : "application/json"}

        })

        setTimeout(() => {

            pinia.getCategorias()

        }, 400)

    }


</script>

<style lang="scss" scoped>

    .categoria{

        @include tablas();

        &-title{

            @include title-tabla();

        }
        
        &-tabla{

            width: 100%;
            height: 90%;

            table{

                width: 100%;

                th,td{

                    @include celdas('20%');

                }

                td:nth-child(1){

                    @include celdas('60%')

                }

                .categoria-tabla-btn-actualizar{

                    color: $fondo-boton-crear;
                    cursor: pointer;

                }

                .categoria-tabla-btn-eliminar{

                    color: $fondo-boton-eliminar;
                    cursor: pointer;

                }

            }

        }

        &-nuevo{

            @include div-boton-crear();

            button{

                @include botones($fondo-boton-crear);

            }

        }

    }

</style>
