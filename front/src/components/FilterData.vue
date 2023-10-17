<template>
    <section class="filtrar-informacion">
        <div class="filtrar-informacion-buscar">
            <h1 class="filtrar-informacion-buscar-titulo"> Buscar producto </h1>
            <div class="filtrar-informacion-buscar-boton">
                <input v-model="busqueda" type="text" placeholder="Nombre">
                <button @click="buscar" > Buscar </button>
            </div>
        </div>
        <div class="filtrar-informacion-categoria">
            <h1 class="filtrar-informacion-categoria-titulo"> Filtrar por categoria </h1>
            <ul>
                <li 
                    @click="pinia.listaProductosFiltrar = pinia.listaProductos,
                    pinia.listaProductosPagina = pinia.listaProductos"
                > Todas </li>
               <li 
                    v-for="(cate, i) in pinia.listaCategorias" :key="i"
                    @click="filtrar(cate.nombre)">
                    {{ cate.nombre }}
               </li> 
            </ul>
        </div>
        <div class="filtrar-informacion-precio">
            <h1 class="filtrar-informacion-precio-titulo"> Filtrar por precio </h1>
            <li @click="precio=true" class="filtrar-informacion-precio-mayor">
                Mayor precio: 
                <v-icon name="bi-arrow-down-square-fill" scale="1.2" flip="vertical"></v-icon>
            </li>
            <li @click="precio=false" class="filtrar-informacion-precio-menor">
                Menor precio: 
                <v-icon name="bi-arrow-down-square-fill" scale="1.2"></v-icon>
            </li>
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
      
            pinia.listaProductosPagina = pinia.listaProductosFiltrar.sort(
                
                (a, b) => b.precio - a.precio
            
            )

        }else{

            pinia.listaProductosPagina = pinia.listaProductosFiltrar.sort(
                
                (a, b) => a.precio - b.precio
            
            )

        }

    })

</script>

<style lang="scss" scoped>

    .filtrar-informacion{

        width: 15%;
        position: sticky;
        top: 0;
        display: flex;
        flex-direction: column;
        justify-content: space-evenly;
        align-items: center;
        background: $fondo-div;
        box-sizing: border-box;
        border-radius: 10px;
        height: 95%;
        overflow: auto;

        &-buscar{

            width: 80%;
            height: 20%;
            display: flex;
            flex-direction: column;
            border-bottom: 2px solid #fff;

            &-titulo{

                text-align: center;
                color: #fff;
                font-size: 35px;
                margin-bottom: 20px;

            }

            &-boton{

                display: flex;
                width: 100%;
                justify-content: space-evenly;

                input{

                    width: 50%;
                    border: 0;
                    padding: 10px;
                    background: #eee;
                    border-radius: 10px;
                    height: max-content;
    
                }
    
                button{
    
                    @include botones('#fff');
                    color: #000;
                    font-weight: 100;
                    height: max-content;
    
                }
    
                button:hover{
    
                    background: #ddd;
    
                }

            }

        }

        &-categoria{

            width: 100%;
            height: 40%;
            overflow: auto;
            display: flex;
            flex-direction: column;
            align-items: center;

            &-titulo{

                text-align: center;
                color: #fff;
                font-size: 35px;
                margin-bottom: 20px;

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

        &-precio{

            width: 80%;
            height: 20%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            border-top: 2px solid #fff;

            &-titulo{

                text-align: center;
                color: #fff;
                font-size: 35px;

            }

            &-mayor{

                width: 80%;
                height: max-content;
                margin: 10px 0;
                display: flex;
                justify-content: space-evenly;
                font-size: 20px;
                color: #fff;
                cursor: pointer;

            }

            &-mayor:hover{

                color: #bbb;
    
            }

            &-menor{

                width: 80%;
                height: 20%;
                margin: 10px 0;
                display: flex;
                justify-content: space-evenly;
                font-size: 20px;
                color: #fff;
                cursor: pointer;

            }

            &-menor:hover{

                color: #bbb;

            }

        }

    }

</style>