<template>
    <section class="service">
        <div class="service-title">
            <h1> Tabla servicios </h1>
        </div>
        <div class="service-tabla">
            <table>
                <thead>
                    <tr>
                        <th> Nombre </th>
                        <th> Descripcion </th>
                        <th> Imagen </th>
                        <th> Precio </th>
                        <th> Actualizar informacion </th>
                        <th> Eliminar </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(service, i) in pinia.listaServiciosFiltrar" :key="i">
                        <td> {{ service.nombre }} </td>
                        <td> {{ service.descripcion }} </td>
                        <td class="imagen">
                            <img :src="service.img" alt="">
                        </td>
                        <td> {{ service.precio }} </td>
                        <td>

                            <router-link 
                                class="service-tabla-btn-actualizar" 
                                :to="{name: 'servicio', params: { id: service.id}}">
                                <v-icon  
                                    name="md-changecircle-round" 
                                    scale="2">
                                </v-icon>  
                            </router-link>

                        </td>
                        <td 
                            class="service-tabla-btn-eliminar"> 
                            <v-icon 
                                @click="eliminarServicio(service.id)"
                                name="md-delete" 
                                scale="2">
                            </v-icon> 
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="service-nuevo">
            <button @click="nuevoServicio"> Nuevo servicio </button>
        </div>
    </section>
</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia';

    import { defineEmits } from 'vue';

    const emits = defineEmits(['mostrarInterfaz'])

    const nuevoServicio = () => emits('mostrarInterfaz', 'servicio')

    const pinia = useStore()

    function eliminarServicio(id: number){

        fetch(`http://127.0.0.1:8000/api/Servicio/${id}/`, {

            method: 'DELETE',
            headers: {"content-type" : "application/json"}

        })

        setTimeout(() => {

            pinia.getServicios()

        }, 400)

    }

</script>

<style lang="scss" scoped>

    .service{

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

                    @include celdas('10%');

                }

                td:nth-child(2){

                    @include celdas('50%')

                }

                .imagen{

                    @include celdas('10%')

                }

                .service-tabla-btn-actualizar{

                    color: $fondo-boton-crear;
                    cursor: pointer;

                }

                .service-tabla-btn-eliminar{

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
