<template>
    <div class="new-product" :style="{background: pinia.fondoEdits}">
        
        <h1 class="new-product-title"> Nuevo producto </h1>
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
        <div class="new-product-campo">
            <label> Imagen ilustrativa del producto:  </label>
            <input type="file" :onchange="imagenValor">
        </div>
        <div class="new-product-campo">
            <label> Descripcion del producto:  </label>
            <textarea v-model="descripcion" rows="5"></textarea>
        </div>
        <div class="new-product-campo">
            <label> Cantidad de unidades del producto:  </label>
            <input v-model="cantidad" type="text" placeholder="Cantidad">
        </div>
        <div class="new-product-campo">
            <label> Precio del producto:  </label>
            <input v-model="precio" type="text" placeholder="Precio">
        </div>
        <div class="new-product-button">
            <button 

                :style="{background: pinia.fondoRed}" 
                @click="emits('cerrar')"> Cancelar 

            </button>

            <button 

                :style="{background: pinia.greentheme}" 
                @click="nuevoProducto"> Crear 

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

    const imagenValor = (img) => imagen.value = img.target.files[0]

    function nuevoProducto(){

        let bodyForm = new FormData()

        bodyForm.append('nombre', nombre.value)
        bodyForm.append('categoria', categoria.value)
        bodyForm.append("img", imagen.value)
        bodyForm.append('descripcion', descripcion.value)
        bodyForm.append('cantidad', cantidad.value)
        bodyForm.append('precio', precio.value)

        fetch(`http://127.0.0.1:8000/post/product/`, {

            method: 'POST',
            body: bodyForm

        });

        emits('cerrar')

        setTimeout(() => {

            pinia.getProductos()
            nombre.value = ""
            categoria.value = "1"
            descripcion.value = "Descripcion"
            cantidad.value = 1
            precio.value = 1

        }, 600)
        
    }

</script>

<style lang="scss" scoped>

    .new-product{

        height: 90%;
        width: 30%;
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
            justify-content: space-between;
            align-items: flex-end;

            button{

                @include botones();
                height: max-content;

            }

        }

    }

</style>