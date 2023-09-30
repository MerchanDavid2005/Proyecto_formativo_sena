<template>
    <div class="products-all">
        
        <div v-for="(prd, i) in pinia.listaProductosPagina.slice(0, 12)" :key="i">
            <h1> {{ prd.nombre }} </h1>
            <p> <strong> Categoria:  </strong> {{ prd.categoria }} </p>
            <article class="imagen">
                <img :src="prd.img" alt="">
            </article>
            <p class="products-all-descripcion"> <strong> Descripcion:  </strong> {{ prd.descripcion }} </p>
            <p> <strong> Cantidad:  </strong> {{ prd.cantidad }} </p>
            <p> <strong> Precio:  </strong> {{ prd.precio }} </p>
        </div>

        <div class="contenedor-compras-paginas">
            <router-link 
                :class="{'urls': router.params.id != pag, 'url-selected': router.params.id == pag}"
                v-for="(pag, i) in numeroPaginas" 
                :key="i" 
                :to="{name : 'productos', params: {id: pag}}">

                {{ pag }}
            </router-link>
        </div>

    </div>
</template>

<script lang="ts" setup> 

    import { useRoute, useRouter } from 'vue-router';
    import { useStore } from '../store/pinia';
    import { ref, onUpdated } from 'vue'

    const router = useRoute()
    const enrutado = useRouter()
    const pinia = useStore()

    let paginaAnterior = ref<number>(1)

    let numeroPaginas = ref<Array<string>>(["1"])

    function traerDatos(){

        if(typeof(router.params.id) == "string"){

            paginaAnterior.value = parseInt(router.params.id, 10) - 1
            pinia.listaProductosPagina = pinia.listaProductosFiltrar.slice(

                paginaAnterior.value * 12,
                parseInt(router.params.id) * 12

            )

        }

        let paginas = []

        for(let i = 0; i < pinia.listaProductosFiltrar.length / 12; i++){
            paginas.push(`${i + 1}`)
        }

        numeroPaginas.value = paginas

    }

    onUpdated(() => {

        traerDatos()

    })

    traerDatos()

</script>

<style lang="scss" scoped>

    .products-all{

        width: 80%;
        height: max-content;
        box-sizing: border-box;
        display: flex;
        justify-content: space-evenly;
        flex-wrap: wrap;

        div{

            width: 30%;
            height: 600px;
            box-sizing: border-box;

            h1{

                text-align: center;
                margin-bottom: 35px;

            }

            .imagen{

                width: 100%;
                height: 30%;
                margin: 20px 0;

            }

            p{

                margin: 20px 0;
                font-size: 18px;

            }

            &-descripcion{

                height: 30%;
                overflow: auto;

            }

        }

        .contenedor-compras-paginas{

            width: 100%;
            height: max-content;
            display: flex;
            justify-content: center;
            position: sticky;
            bottom: 5vh;

            .urls{

                padding: 1vh 2vh;
                margin: 0 5px;
                text-decoration: none;
                border-radius: 10px;
                background: #eee;
                color: #000;

            }

            .url-selected{

                padding: 1vh 2vh;
                margin: 0 5px;
                text-decoration: none;
                border-radius: 10px;
                background: $fondo-boton-limpiar;
                color: #fff;

            }

        }

    }

</style>