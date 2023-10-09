<template>
    <div class="edit-product" :style="{background: pinia.fondoEdits}">
        
        <h1 class="edit-product-title"> Editar producto </h1>
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
        <div class="edit-product-campo">
            <label> Imagen ilustrativa del producto:  </label>
            <input type="file" :onchange="imagenValor">
        </div>
        <div class="edit-product-campo">
            <label> Descripcion del producto:  </label>
            <textarea v-model="descripcion" rows="5"></textarea>
        </div>
        <div class="edit-product-campo">
            <label> Cantidad de unidades del producto:  </label>
            <input v-model="cantidad" type="text" placeholder="Cantidad">
        </div>
        <div class="edit-product-campo">
            <label> Precio del producto:  </label>
            <input v-model="precio" type="text" placeholder="Precio">
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

    const imagenValor = (img) => imagen.value = img.target.files[0]

    function editarProducto(){

        let producto = pinia.listaProductos[ruta.params.id]

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

        }, 600)

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

        &-campo{

            margin-bottom: 10px;

            input, textarea, select{

                @include inputs();

            }

        }

        &-campo:nth-child(4){

            display: flex;
            flex-direction: column;

            input{

                margin: 10px 0;

            }

        }

        &-campo:nth-child(5){

            display: flex;
            flex-direction: column;

            textarea{

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

</style>