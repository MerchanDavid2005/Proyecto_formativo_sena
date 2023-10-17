<template>
    <section class="filtrar-informacion">
        <h1> Buscar producto </h1>
        <div class="filtrar-informacion-buscar">
            <input v-model="busqueda" type="text" placeholder="Nombre">
            <button @click="buscar" > Buscar </button>
        </div>
        <h1> Filtrar por categoria </h1>
        <div>
            <ul>
                <li 
                    @click="pinia.listaCategoriasFiltrar = pinia.listaCategorias,
                    pinia.listaProductosFiltrar = pinia.listaProductos,
                    pinia.listaProductosPagina = pinia.listaProductos,
                    pinia.carritoFiltrar = pinia.carrito"
                > Todas </li>
               <li 
                    v-for="(cate, i) in pinia.listaCategorias" :key="i"
                    @click="filtrar(cate.nombre)">
                    {{ cate.nombre }}
               </li> 
            </ul>
        </div>
        <div>
            <h1> Filtrar por precio </h1>
            <div @click="precio=true" class="filtrar-informacion-precio">
                <label> Mayor precio: </label>
                <v-icon name="bi-arrow-down-square-fill" scale="1.2" flip="vertical"></v-icon>
            </div>
            <div @click="precio=false" class="filtrar-informacion-precio">
                <label> Menor precio: </label>
                <v-icon name="bi-arrow-down-square-fill" scale="1.2"></v-icon>
            </div>
        </div>
    </section>
</template>

<script lang="ts" setup>

    import { ref, watch } from 'vue';
    import { useStore } from '../store/pinia';

    const pinia = useStore()

    let busqueda = ref<string>("")
    let precio = ref<boolean>(false)

    const buscar = () => {

        pinia.listaProductosFiltrar = pinia.listaProductos.filter(
            i => i.nombre.toLowerCase().startsWith(busqueda.value.toLowerCase())
        )

        pinia.listaProductosPagina = pinia.listaProductos.filter(
            i => i.nombre.toLowerCase().startsWith(busqueda.value.toLowerCase())
        )

        pinia.carritoFiltrar = pinia.carrito.filter(
            i => i.nombre.toLowerCase().startsWith(busqueda.value.toLowerCase())
        )

    }

    const filtrar = (categoria: string) => {

        pinia.listaProductosFiltrar = pinia.listaProductos.filter(i => i.categoria == categoria)
        pinia.listaCategoriasFiltrar = pinia.listaCategorias.filter(i => i.nombre == categoria)

        pinia.listaProductosPagina = pinia.listaProductos.filter(i => i.categoria == categoria)
        pinia.carritoFiltrar = pinia.carrito.filter(i => i.categoria == categoria)

    }

    watch(precio, () => {

        if(precio.value){

            pinia.listaProductosFiltrar = pinia.listaProductosFiltrar.sort(
                
                (a, b) => a.precio - b.precio
            
            )

        }else{

            pinia.listaProductosFiltrar = pinia.listaProductosFiltrar.sort(
                
                (a, b) => b.precio - a.precio
            
            )

        }

    })

</script>

<style lang="scss" scoped>

    .filtrar-informacion{

        @include barras-laterales('15%');
        overflow: auto;

        h1{

            text-align: center;
            color: #fff;
            font-size: 30px;
            margin-bottom: 20px;

        }

        &-buscar{

            width: 100%;
            height: max-content;
            display: flex;
            justify-content: space-evenly;
            margin: 30px 0;

            input{

                width: 50%;
                border: 0;
                padding: 10px;
                background: #eee;
                border-radius: 10px;

            }

            button{

                @include botones('#fff');
                color: #000;
                font-weight: 100;

            }

            button:hover{

                background: #ddd;

            }

        }

        ul{

            list-style: none;
            padding-top: 40px;

            li{

                font-size: 20px;
                cursor: pointer;
                margin-bottom: 20px;
                color: #fff;

            }
            
            li:hover{

                color: #bbb;

            }

        }

        &-precio{

            width: 80%;
            display: flex;
            justify-content: space-evenly;
            align-items: center;
            color: #fff;
            height: max-content;
            margin: 20px 0;
            font-size: 20px;

        }

    }

</style>