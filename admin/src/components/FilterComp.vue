<template>
    <div class="filtrar">
        
        <div class="filtrar-nombre">
            <h1> Buscar: </h1>
            <div>
                <input v-model="producto" type="text" placeholder="Nombre producto">
                <button @click="buscar"> Buscar </button>
            </div>
        </div>

        <div class="filtrar-categoria">

            <h1> Filtrar </h1>
            <ul>
                <li @click="todos"> Todos </li>
                <li @click="filtrar(cate.nombre)" v-for="(cate, i) in pinia.listaCategorias" :key="i">

                    {{ cate.nombre }}

                </li>
            </ul>

        </div>

    </div>
</template>

<script setup>

    import { useStore } from '@/store/pinia'
    import { ref } from 'vue'

    const pinia = useStore()

    let producto = ref("")

    const buscar = () => {

        pinia.listaProductosFilter = pinia.listaProductos.filter(
            i => i.nombre.toLowerCase().startsWith(producto.value.toLowerCase())
        )

        pinia.listaCategoriasFilter = pinia.listaCategorias.filter(
            i => i.nombre.toLowerCase().startsWith(producto.value.toLowerCase())
        )

    }

    const todos = () => {

        pinia.listaProductosFilter = pinia.listaProductos
        pinia.listaCategoriasFilter = pinia.listaCategorias
            
    }

    const filtrar = (categoria) => {

        pinia.listaProductosFilter = pinia.listaProductos.filter(i => i.categoria == categoria)
        pinia.listaCategoriasFilter = pinia.listaCategorias.filter(i => i.nombre == categoria)

    }

</script>

<style lang="scss" scoped>

    .filtrar{

        width: 15%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-evenly;
        background: $second-color;
        color: #fff;
        border-radius: 10px;
        position: sticky;
        top: 0;

        &-nombre{

            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 10px;
            height: 20%;

            div{

                display: flex;
                justify-content: space-between;
                align-items: center;
                width: 100%;
                margin: 20px 0;

                input{

                    @include inputs();
                    width: 60%;

                }

                button{

                    @include botones($first-color);

                }

            }

        }

        &-categoria{

            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 10px;
            height: 60%;
            overflow: auto;

            ul{

                list-style: none;
                width: 100%;
                display: flex;
                flex-direction: column;
                align-items: center;

                li{

                    font-size: 20px;
                    margin: 10px 0;
                    cursor: pointer;

                }

            }

        }

    }

</style>