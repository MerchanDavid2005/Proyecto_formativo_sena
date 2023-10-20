<template>
    <div class="products-all">

        <div class="products-all-prd">

            <h1 v-if="pinia.listaProductosPagina.length < 1"> No hay resultados de tu busqueda </h1>
        
            <div class="products-all-prd-product" v-for="(prd, i) in pinia.listaProductosPagina" :key="i">
                <h1> {{ prd.nombre }} </h1>
                <p> <strong> Categoria:  </strong> {{ prd.categoria }} </p>
                <article class="products-all-prd-product-imagen">
                    <img :src="prd.img" alt="">
                </article>
                <p class="products-all-prd-product-descripcion"> <strong> Descripcion:  </strong> {{ prd.descripcion }} </p>
                <p> <strong> Cantidad:  </strong> {{ prd.cantidad }} </p>
                <p> <strong> Precio:  </strong> {{ prd.precio }} </p>
                <button @click="comprar(prd.id)"> 
                    Añadir al carrito 
                    <v-icon style="margin-left: 5px" name="bi-cart-plus-fill" scale="1.3"></v-icon>
                </button>
            </div>

        </div>

        <div class="products-all-pagination">
            <p
                v-for="(pag, i) in listaPaginas" 
                :key="i"
                @click="pinia.cambiarPagina(i + 1)"
                :class="{'urls': pinia.paginaActual != pag, 'url-selected': pinia.paginaActual == pag}">
                {{ pag }}
            </p>
        </div>

    </div>
</template>

<script lang="ts" setup> 

    import { useStore } from '../store/pinia';
    import { defineEmits, onMounted, computed } from 'vue'

    const pinia = useStore()
    const emits = defineEmits(['verificar'])

    const comprar = async (id: number) => {

        const prd = await fetch(`http://localhost:8000/get/product/${id}/`)
        const data = await prd.json()

        pinia.productoVerificar = data.producto

        emits('verificar') 

    }

    const listaPaginas = computed(() => {

        let paginas = []

        for(let i = 0; i < Math.ceil(pinia.listaProductosFiltrar.length / 12); i++){

            paginas.push(`${i + 1}`)

        }

        return paginas

    })

    onMounted(() => {

        pinia.cambiarPagina(1);

    })

</script>

<style lang="scss" scoped>

    .products-all{

        width: 80%;
        height: max-content;
        display: flex;
        flex-direction: column;
        align-items: center;

        &-prd{

            width: 100%;
            height: 100%;
            box-sizing: border-box;
            display: flex;
            justify-content: space-evenly;
            flex-wrap: wrap;

            &-product{

                width: 30%;
                height: 500px;
                box-sizing: border-box;
                display: flex;
                flex-direction: column;
                margin: 20px 0;
                transition: transform 0.5s ease-in-out;
    
                h1{
    
                    text-align: center;
                    margin-bottom: 20px;
    
                }
    
                &-imagen{
    
                    width: 100%;
                    height: 30%;
                    margin: 10px 0;
    
                }

                p{
    
                    margin: 10px 0;
                    font-size: 15px;
    
                }
    
                &-descripcion{
    
                    height: 15%;
                    overflow: auto;
    
                }
    
                button{
    
                    @include botones($fondo-boton-crear);
                    align-self: center;
                    width: 55%;
                    font-size: 15px;
                    padding: 10px;
                    margin-top: 10px;
    
                }
    
            }

            &-product:hover{

                transform: scale(1.05);

            }

        }

        &-pagination{

            width: max-content;
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
                cursor: pointer;

            }

            .url-selected{

                padding: 1vh 2vh;
                margin: 0 5px;
                text-decoration: none;
                border-radius: 10px;
                background: $fondo-boton-limpiar;
                color: #fff;
                cursor: pointer;

            }

        }

    }

</style>