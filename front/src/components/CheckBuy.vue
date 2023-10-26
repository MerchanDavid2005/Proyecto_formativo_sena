<template>
    <div class="interfaz-verificar-compra">
        
        <section class="interfaz-verificar-compra-datos">

            <h1> {{ pinia.productoVerificar.nombre }} </h1>
            <p> <strong> Categoria: </strong> {{ pinia.productoVerificar.categoria }} </p>
            <p class="interfaz-verificar-compra-datos-descripcion"> <strong> Descripcion: </strong> {{ pinia.productoVerificar.descripcion }} </p>
            <p> <strong> Cantidad disponible: </strong> {{ pinia.productoVerificar.cantidad }} </p>
            <div class="interfaz-verificar-compra-datos-cantidad">
                <p> <strong> Cantidad: </strong> {{ cantidad }} </p>
                <button 
                    class="interfaz-verificar-compra-datos-cantidad-mas" 
                    @click="sumar" 
                    v-if="cantidad < pinia.productoVerificar.cantidad"> + </button>
                <button 
                    class="interfaz-verificar-compra-datos-cantidad-menos" 
                    @click="restar" 
                    v-if="cantidad > 1"> - </button>
            </div>
            <p> <strong> Precio total: </strong> {{ precio }} </p>
            <div class="interfaz-verificar-compra-datos-botones">
                <button 
                    @click="cerrar" 
                    class="interfaz-verificar-compra-datos-botones-cerrar"> 
                    Volver 
                    <v-icon name="bi-cart-x-fill" scale="1.5"></v-icon>
                </button>
                <button 
                    @click="actualizar"
                    v-if="cantidad > 0"
                    class="interfaz-verificar-compra-datos-botones-verificar"> 
                    Verificar 
                    <v-icon name="bi-cart-check-fill" scale="1.5"></v-icon>
                </button>    
            </div>

        </section>

        <section class="interfaz-verificar-compra-imagen">

            <img :src="pinia.productoVerificar.img" :alt="`Producto ${pinia.productoVerificar.nombre}`" >

        </section>

    </div>
</template>

<script lang="ts" setup>

    import { ref, defineEmits } from 'vue'
    import { useStore } from '../store/pinia'

    const pinia = useStore()
    const emits = defineEmits(['ocultar', 'animacion'])

    let cantidad = ref<number>(0)
    let precio = ref<number>(0)

    const sumar = () => {

        cantidad.value++
        precio.value += pinia.productoVerificar.precio 

    }

    const restar = () => {

        cantidad.value--
        precio.value -= pinia.productoVerificar.precio 

    }

    const comprar = async () => {

        emits('ocultar');
        emits('animacion');

        let productoRepetido = false
        let idProductoRepetido = 0

        let productoComprado = {
            
            id: pinia.productoVerificar.id,
            nombre: pinia.productoVerificar.nombre,
            categoria: pinia.productoVerificar.categoria,
            img: pinia.productoVerificar.img,
            descripcion: pinia.productoVerificar.descripcion,
            cantidad: cantidad.value,
            precio: precio.value
        
        }

        for(let i in pinia.datosUsuario.carrito){

            if(pinia.datosUsuario.carrito[i].nombre == productoComprado.nombre){

                productoRepetido = true
                idProductoRepetido = Number(i)
                break

            }

        }

        if(productoRepetido){

            pinia.datosUsuario.carrito[idProductoRepetido].cantidad += productoComprado.cantidad
            pinia.datosUsuario.carrito[idProductoRepetido].precio += productoComprado.precio

            const data = await fetch(`http://localhost:8000/api/Usuario/${pinia.datosUsuario.id}/`, {

                method: 'PATCH',
                body: JSON.stringify({

                    carrito: JSON.stringify(pinia.datosUsuario.carrito)

                }),
                headers: {"content-type": "application/json"}

            })

            return data.json()


        }else{

            pinia.datosUsuario.carrito.push(productoComprado)

            const data = await fetch(`http://localhost:8000/api/Usuario/${pinia.datosUsuario.id}/`, {

                method: 'PATCH',
                body: JSON.stringify({

                    carrito: JSON.stringify(pinia.datosUsuario.carrito)

                }),
                headers: {"content-type": "application/json"}

            })

            return data.json()

        }

    }

    const actualizar = async () => {

        await comprar()

        cantidad.value = 0
        precio.value = 0
        pinia.getUsuario(pinia.datosUsuario.id)

    }

    const cerrar = () => {

        emits('ocultar')
        
        setTimeout(() => {

            cantidad.value = 0
            precio.value = 0
            
        }, 500)

    }

</script>

<style lang="scss" scoped>

    .interfaz-verificar-compra{

        position: static;
        z-index: 5000;
        width: 50%;
        height: 70%;
        padding: 3%;
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        background: #fff;
        outline: 2px solid #000;
        border-radius: 10px;

        section{

            width: 45%;
            height: 100%;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            align-items: center;

            h1{

                font-size: 30px;
                margin-bottom: 20px;

            }

            p{

                align-self: flex-start;
                margin: 15px 0;
                font-size: 18px;

            }   

            .interfaz-verificar-compra-datos-descripcion{

                height: 30%;
                overflow: auto;

            }

            .interfaz-verificar-compra-datos-cantidad{

                align-self: flex-start;
                display: flex;
                align-items: center;
                justify-content: flex-start;

                &-mas{

                    @include botones($fondo-boton-crear);
                    margin-left: 10px;
                    padding: 5px 10px;
                    font-size: 20px;
    
                }
    
                &-menos{
    
                    @include botones($fondo-boton-eliminar);
                    margin-left: 10px;
                    padding: 5px 10px;
                    font-size: 20px;
    
                }

            }

            .interfaz-verificar-compra-datos-botones{

                width: 100%;
                display: flex;
                justify-content: space-evenly;
                margin-top: 30px;

                &-verificar{

                    @include botones($fondo-boton-crear);
                    font-size: 20px;
                    padding: 15px;

                }

                &-cerrar{

                    @include botones($fondo-boton-eliminar);
                    font-size: 20px;
                    padding: 15px;

                }

            }

        }

    }

</style>