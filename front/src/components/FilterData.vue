<template>
    <section class="filtrar-informacion">
        <h1> Buscar producto </h1>
        <div class="filtrar-informacion-buscar">
            <input v-model="busqueda" type="text" placeholder="Nombre">
            <button @click="buscar" > Buscar </button>
        </div>
        <h1> Filtrar por categoria </h1>
        <ul>
            <li 
                @click="pinia.listaCategoriasFiltrar = pinia.listaCategorias,
                pinia.listaProductosFiltrar = pinia.listaProductos,
                pinia.listaProductosPagina = pinia.listaProductos"
            > Todas </li>
           <li 
                v-for="(cate, i) in pinia.listaCategorias" :key="i"
                @click="filtrar(cate.nombre)">
                {{ cate.nombre }}
           </li> 
        </ul>
    </section>
</template>

<script lang="ts" setup>

    import { ref } from 'vue';
    import { useStore } from '../store/pinia';

    const pinia = useStore()

    let busqueda = ref<string>("")

    const buscar = () => {

        pinia.listaProductosFiltrar = pinia.listaProductos.filter(
            i => i.nombre.toLowerCase().startsWith(busqueda.value.toLowerCase())
        )

        pinia.listaProductosPagina = pinia.listaProductos.filter(
            i => i.nombre.toLowerCase().startsWith(busqueda.value.toLowerCase())
        )

    }

    const filtrar = (categoria: string) => {

        pinia.listaProductosFiltrar = pinia.listaProductos.filter(i => i.categoria == categoria)
        pinia.listaCategoriasFiltrar = pinia.listaCategorias.filter(i => i.nombre == categoria)

        pinia.listaProductosPagina = pinia.listaProductos.filter(i => i.categoria == categoria)

    }

</script>

<style lang="scss" scoped>

    .filtrar-informacion{

        @include barras-laterales('15%');
        overflow: auto;

        h1{

            text-align: center;
            color: #fff;

        }

        &-buscar{

            width: 100%;
            height: max-content;
            display: flex;
            justify-content: space-evenly;
            margin: 50px 0;

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

    }

</style>