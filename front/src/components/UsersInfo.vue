<template>
    <section class="productos">
        <div class="productos-title">
            <h1> Tabla Usuarios </h1>
        </div>
        <div class="productos-tabla">
            <p 
                style="text-align: center; margin:20px 0;"
                v-if="pinia.listaUsuariosFiltrar.length < 1
                "> 
                No hay resultados de tu busqueda 
            </p>
            <div class="productos-tabla-buscar">
                <label> Buscar por usuario:  </label>
                <input v-model="nombre" type="text" placeholder="Ingresa el nombre del usuario">
                <button @click="filtrar">
                    Buscar
                </button>
            </div>
            <table>
                <thead>
                    <tr>
                        <th> Usuario </th>
                        <th> Nombre </th>
                        <th> Email </th>
                        <th> Rol </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(user, i) in pinia.listaUsuariosFiltrar" :key="i">
                        <td> {{ user.nombre_usuario }} </td>
                        <td> {{ user.nombre }} </td>
                        <td> {{ user.email }} </td>
                        <td> {{ user.rol }} </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>
</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia';
    import { ref } from 'vue';

    const pinia = useStore()
    
    let nombre = ref<string>("")

    const filtrar = () => {

        pinia.listaUsuariosFiltrar = pinia.listaUsuarios.filter(i => i.nombre_usuario.toLowerCase().startsWith(nombre.value.toLowerCase()))

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

            &-buscar{

                margin: 10px 0;

                input{

                    @include inputs();
                    width: 20%;
                    margin-right: 10px;

                }

                button{

                    @include botones($fondo-boton-limpiar)

                }

            }

            table{

                width: 100%;

                th, td{

                    @include celdas('15%')

                }
                
                th:nth-child(3), td:nth-child(3){

                    @include celdas('50%')

                }

            }

        }

    }
</style>
