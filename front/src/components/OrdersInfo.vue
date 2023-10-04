<template>
    <section class="productos">
        <div class="productos-title">
            <h1> Tabla pedidos </h1>
        </div>
        <div class="productos-tabla">
            <p 
                style="text-align: center; margin:20px 0;"
                v-if="pinia.listaPedidosFiltrar.length < 1
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
                        <th> Lista productos </th>
                        <th> Fecha </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(order, i) in pinia.listaPedidosFiltrar" :key="i">
                        <td> {{ order.nombre }} </td>
                        <td>
                            <button @click="informacionPedido(order.id)"> Ver informacion de la compra </button>
                        </td>
                        <td>
                            <span> Dia: {{ order.fecha.slice(0,10) }} / </span>
                            <span> Hora: {{ order.fecha.slice(11, 16) }} </span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>
</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia';
    import { useRouter } from 'vue-router';
    import { ref } from 'vue';

    const pinia = useStore()
    const enrutado = useRouter()

    let nombre = ref<string>("")
    
    const informacionPedido = (id: number) => enrutado.push(`/pedido/${id}`)

    const filtrar = () => {

        pinia.listaPedidosFiltrar = pinia.listaPedidos.filter(i => i.nombre.toLowerCase().startsWith(nombre.value.toLowerCase()))

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

                th:nth-child(1), td:nth-child(1){

                    @include celdas('15%')

                }

                th:nth-child(2), td:nth-child(2){

                    @include celdas('50%');

                    button{

                        @include botones($fondo-boton-crear);

                    }

                }
                
                th:nth-child(3), td:nth-child(3){

                    @include celdas('25%')

                }

            }

        }

    }
</style>
