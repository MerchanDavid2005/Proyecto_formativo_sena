<template>
    <section class="filtrar">
        <div class="filtrar-informacion">
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
                        pinia.listaProductosPagina = pinia.listaProductosFiltrar.slice(0, 12)"
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
        );
        pinia.listaProductosPagina = pinia.listaProductosFiltrar.slice(0, 12);
        pinia.cambiarPagina(1);

    }

    const filtrar = (categoria: string) => {

        pinia.listaProductosFiltrar = pinia.listaProductos.filter(i => i.categoria == categoria);
        pinia.listaProductosPagina = pinia.listaProductosFiltrar.slice(0, 12);
        pinia.cambiarPagina(1);

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

    .filtrar{

        width: 15%;
        position: sticky;
        top: 0;
        height: 95%;
        box-sizing: border-box;
        border-radius: 10px;
        background: $fondo-div;
        overflow: auto;

        &-informacion{

            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            height: max-content;

            &-buscar{

                width: 80%;
                height: 30vh;
                display: flex;
                flex-direction: column;
                justify-content: space-evenly;
                border-bottom: 2px solid #fff;
    
                &-titulo{
    
                    text-align: center;
                    color: #fff;
                    font-size: 30px;
                    margin-bottom: 10px;
    
                }
    
                &-boton{
    
                    display: flex;
                    width: 100%;
                    justify-content: space-between;
    
                    input{
    
                        width: 45%;
                        border: 0;
                        background: #eee;
                        border-radius: 10px;
                        height: max-content;
                        padding: 10px;
        
                    }
        
                    button{
        
                        @include botones('#fff');
                        color: #000;
                        font-weight: 100;
                        height: max-content;
                        width: 35%;
        
                    }
        
                    button:hover{
        
                        background: #ddd;
        
                    }
    
                }
    
            }
    
            &-categoria{
    
                width: 90%;
                height: max-content;
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 10px 0;
    
                &-titulo{
    
                    text-align: center;
                    color: #fff;
                    font-size: 30px;
                    margin-bottom: 10px;
    
                }
    
                ul{
    
                    list-style: none;
                    padding-top: 20px;
        
                    li{
        
                        font-size: 18px;
                        cursor: pointer;
                        margin-bottom: 15px;
                        color: #fff;
        
                    }
                    
                    li:hover{
        
                        color: #bbb;
        
                    }
        
                }
    
            }
    
            &-precio{
    
                width: 90%;
                height: 20vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                border-top: 2px solid #fff;
                overflow: auto;
                padding-top: 15px;
    
                &-titulo{
    
                    text-align: center;
                    color: #fff;
                    font-size: 25px;
    
                }
    
                &-mayor{
    
                    width: 80%;
                    height: max-content;
                    margin: 10px 0;
                    display: flex;
                    justify-content: space-evenly;
                    font-size: 15px;
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
                    font-size: 15px;
                    color: #fff;
                    cursor: pointer;
    
                }
    
                &-menor:hover{
    
                    color: #bbb;
    
                }
    
            }
    

        }

    }

    @media(min-width:1600px){


        .filtrar-informacion-buscar{

            height: 20vh;

        }
        .filtrar-informacion-precio{

            height: 15vh;

        }

    }

</style>