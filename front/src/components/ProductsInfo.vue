<template>
    <section class="productos">
        <div class="productos-title">
            <h1> Tabla productos </h1>
        </div>
        <div class="productos-tabla">
            <p 
                style="text-align: center; margin:20px 0;"
                v-if="pinia.listaProductosFiltrar.length < 1
                "> 
                No hay resultados de tu busqueda 
            </p>
            <table>
                <thead>
                    <tr>
                        <th> Nombre </th>
                        <th> Descripcion </th>
                        <th> Imagen </th>
                        <th> Categoria </th>
                        <th> Cantidad </th>
                        <th> Precio </th>
                        <th> Actualizar informacion </th>
                        <th> Eliminar </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(prd, i) in pinia.listaProductosFiltrar" :key="i">
                        <td> {{ prd.nombre }} </td>
                        <td> {{ prd.descripcion }} </td>
                        <td class="imagen">
                            <img :src="prd.img" alt="">
                        </td>
                        <td> {{ prd.categoria }} </td>
                        <td> {{ prd.cantidad }} </td>
                        <td> {{ prd.precio }} </td>
                        <td> 

                            <router-link 
                                class="productos-tabla-btn-actualizar" 
                                :to="{name: 'producto', params: { id: prd.id}}">
                                <v-icon  
                                    name="md-changecircle-round" 
                                    scale="2">
                                </v-icon>  
                            </router-link>

                        </td>
                        <td > 
                            <v-icon @click="eliminarProducto(prd.id)" 
                                class="productos-tabla-btn-eliminar"
                                name="md-delete" 
                                scale="2">
                            </v-icon> 
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="productos-nuevo">
            <button @click="nuevoProducto"> Nuevo producto </button>
        </div>
    </section>
</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia';

    import { defineEmits } from 'vue';

    const pinia = useStore()

    const emits = defineEmits(['mostrarInterfaz'])

    const nuevoProducto = () => emits('mostrarInterfaz', 'producto')
    
    function eliminarProducto(id: number){

        fetch(`http://127.0.0.1:8000/api/Producto/${id}/`, {

            method: 'DELETE',
            headers: {"content-type" : "application/json"}

        })

        setTimeout(() => {

            pinia.getProductos()

        }, 400)

    }

</script>

<style lang="scss" scoped>

    .productos{

        @include tablas();

        &-title{

            @include title-tabla();

        }
        
        &-tabla{

            width: 100%;
            height: max-content;

            table{

                width: 100%;

                th,td{

                    @include celdas('5%');

                }

                .imagen{

                    @include celdas('10%')

                }

                td:nth-child(2){

                    @include celdas('60%')

                }

                .productos-tabla-btn-actualizar{

                    color: $fondo-boton-crear;
                    cursor: pointer;

                }

                .productos-tabla-btn-eliminar{

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
