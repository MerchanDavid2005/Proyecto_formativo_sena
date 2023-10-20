<template>
    <div class="edit-product" :style="{background: pinia.fondoEdits}">
        
        <h1 class="edit-product-title"> Editar producto </h1>
        <p class="error" v-if="error"> {{ mensajeError }} </p>
        <div class="edit-product-campo">
            <label> Nombre del producto:  </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
        </div>
        <div class="edit-product-campo">
            <label> Categoria del producto:  </label>
            <select v-model="categoria">
                <option v-for="(cate, i) in pinia.listaCategorias" :value="cate.id" :key="i">

                    {{ cate.nombre }}

                </option>
            </select>
        </div>
        <div class="edit-product-campo-selector">
            <label> Imagen ilustrativa del producto:  </label>
            <input type="file" :onchange="imagenValor">
        </div>
        <div class="edit-product-campo-descripcion">
            <label> Descripcion del producto:  </label>
            <textarea v-model="descripcion" rows="5"></textarea>
        </div>
        <div class="edit-product-campo">
            <label> Cantidad de unidades del producto:  </label>
            <input v-model="cantidad" type="number" placeholder="Cantidad">
        </div>
        <div class="edit-product-campo">
            <label> Precio del producto:  </label>
            <input v-model="precio" type="number" placeholder="Precio">
        </div>
        <div class="edit-product-button">
            <button :style="{background: pinia.greentheme}" @click="editarProducto"> Editar </button>
        </div>

    </div>
</template>

<script setup>

    import { useStore } from '@/store/pinia';
    import { ref } from 'vue'
    import { useRoute, useRouter } from 'vue-router';

    const pinia = useStore()
    const ruta = useRoute()
    const enrutado = useRouter()

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

    function editarProducto(){

        let producto = pinia.listaProductos[ruta.params.id]

        if(validar()){

            fetch(`http://127.0.0.1:8000/api/Producto/${producto.id}/`, {

                method: 'PATCH',
                body: JSON.stringify({

                    nombre: nombre.value,
                    categoria: categoria.value,
                    descripcion: descripcion.value,
                    cantidad: cantidad.value,
                    precio: precio.value

                }),
                headers: {"content-type": "application/json"}

            });

            let bodyForm = new FormData()
            bodyForm.append("img", imagen.value)

            fetch(`http://127.0.0.1:8000/put/product/img/${producto.id}/`, {

                method: 'POST',
                body: bodyForm

            });

            enrutado.push('/admin/product')

            setTimeout(() => {

                pinia.getProductos()

            }, 1000)

        }

    }

</script>

<style lang="scss" scoped>

    .edit-product{

        height: 90%;
        width: 30%;
        display: flex;
        flex-direction: column;
        outline: 2px solid #000;
        border-radius: 15px;
        padding: 15px;
        transition: background 0.5s ease;

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

            margin-bottom: 10px;

            input, textarea, select{

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
            justify-content: flex-end;
            align-items: flex-end;

            button{

                @include botones();
                height: max-content;

            }

        }

    }

    @media(min-width: 1600px){

        .edit-product{

            height: 80%;
            width: 30%;

        }

    }

</style>