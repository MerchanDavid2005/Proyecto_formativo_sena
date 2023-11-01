<template>
    <div class="new-product" :style="{background: pinia.fondoEdits}">
        
        <h1 class="new-product-title"> Nuevo producto </h1>
        <p class="error" v-if="error"> {{ mensajeError }} </p>
        <div class="new-product-campo">
            <label> Nombre del producto:  </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
        </div>
        <div class="new-product-campo">
            <label> Categoria del producto:  </label>
            <select v-model="categoria">
                <option v-for="(cate, i) in pinia.listaCategorias" :value="cate.id" :key="i">

                    {{ cate.nombre }}

                </option>
            </select>
        </div>
        <div class="new-product-campo-selector">
            <label> Imagen ilustrativa del producto:  </label>
            <input type="file" :onchange="imagenValor">
        </div>
        <div class="new-product-campo-descripcion">
            <label> Descripcion del producto:  </label>
            <textarea v-model="descripcion" rows="5"></textarea>
        </div>
        <div class="new-product-campo">
            <label> Cantidad de unidades del producto:  </label>
            <input v-model="cantidad" type="number" placeholder="Cantidad">
        </div>
        <div class="new-product-campo">
            <label> Precio del producto:  </label>
            <input v-model="precio" type="number" placeholder="Precio">
        </div>
        <div class="new-product-button">
            <button 

                :style="{background: pinia.fondoRed}" 
                @click="emits('cerrar')"> Cancelar 

            </button>

            <button 

                :style="{background: pinia.greentheme}" 
                @click="cargarDatos"> Crear 

            </button>
        </div>

    </div>
</template>

<script setup>

    import { useStore } from '@/store/pinia';
    import { ref, defineEmits } from 'vue'

    const emits = defineEmits(['cerrar'])
    const pinia = useStore()

    let nombre = ref("")
    let categoria = ref("1")
    let imagen = ref("")
    let descripcion = ref("Descripcion")
    let cantidad = ref(1)
    let precio = ref(1)

    let error = ref(false)
    let mensajeError = ref("")

    const imagenValor = (img) => imagen.value = img.target.files[0]

    function validar(){

        let validado = false

        if(nombre.value != "" && categoria.value != "" && imagen.value != "" && descripcion.value != "" && cantidad.value != "" && precio.value != ""){

            if(imagen.value.name.toLowerCase().endsWith(".png") || 
            imagen.value.name.toLowerCase().endsWith(".jpg") || 
            imagen.value.name.toLowerCase().endsWith(".jpeg")){

                validado = true

            }else{

                error.value = true
                mensajeError.value = "Solo se permiten archivos con extension png, jpg o jpeg"

            }

        }else{

            error.value = true
            mensajeError.value = "No dejes ningun campo en blanco"

        }

        return validado
    
    }

    async function nuevoProducto(){

        let bodyForm = new FormData()

        bodyForm.append('nombre', nombre.value)
        bodyForm.append('categoria', categoria.value)
        bodyForm.append("img", imagen.value)
        bodyForm.append('descripcion', descripcion.value)
        bodyForm.append('cantidad', cantidad.value)
        bodyForm.append('precio', precio.value)

        if(validar()){

            const peticion = await fetch(`http://127.0.0.1:8000/post/product/`, {

                method: 'POST',
                body: bodyForm

            });

            return peticion

        }else{

            return "Error"

        }
        
    }

    async function cargarDatos(){

        pinia.cargandoDatos = true

        try{

            const respuesta = await nuevoProducto()

            if(respuesta !== "Error"){

                emits('cerrar')
                pinia.getProductos()
                nombre.value = ""
                categoria.value = "1"
                descripcion.value = "Descripcion"
                cantidad.value = 1
                precio.value = 1
                pinia.exitoFetch = true
                setTimeout(() => {

                    pinia.exitoFetch = false

                }, 3000)

            }

            pinia.cargandoDatos = false

        }catch(e){

            pinia.cargandoDatos = false
            pinia.errorFetch = true
            setTimeout(() => {

                pinia.errorFetch = false

            }, 3000)

        }

    }

</script>

<style lang="scss" scoped>

    .new-product{

        height: 95%;
        width: 35%;
        display: flex;
        flex-direction: column;
        outline: 2px solid #000;
        border-radius: 15px;
        padding: 15px;
        transition: background 0.5s ease;
        position: absolute;
        z-index: 1000;

        &-title{

            text-align: center;
            margin-bottom: 20px;

        }

        .error{

            text-align: center;
            color: #f00;
            margin-bottom: 20px;

        }

        &-campo{

            margin-bottom: 20px;

            input, select{

                @include inputs();

            }

        }

        &-campo-selector{

            display: flex;
            flex-direction: column;

            input{

                @include inputs();
                margin: 10px 0;
                color: #000;

            }

        }

        &-campo-descripcion{

            display: flex;
            flex-direction: column;

            textarea{

                @include inputs();
                resize: none;
                margin: 10px 0;

            }

        }

        &-button{

            width: 100%;
            height: 100%;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;

            button{

                @include botones();
                height: max-content;

            }

        }

    }

    @media(min-width: 1600px){

        .new-product{

            height: 85%;
            width: 30%;
            
            &-title{

                margin: 20px 0;

            }

        }

    }

</style>