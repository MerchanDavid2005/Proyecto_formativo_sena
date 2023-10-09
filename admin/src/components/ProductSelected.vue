<template>
    <div class="select-product" :style="{background: pinia.fondoEdits}">
        
        <h1 class="select-product-title"> Producto sin editar </h1>
        <div class="select-product-campo">
            <label> Nombre del producto:  </label>
            <input v-model="nombre" type="text" readonly>
        </div>
        <div class="select-product-campo">
            <label> Categoria del producto:  </label>
            <input v-model="categoria" type="text" readonly>
        </div>
        <div class="select-product-campo">
            <label> Imagen ilustrativa del producto:  </label>
            <div>
                <img :src="imagen" :alt="nombre">
            </div>
        </div>
        <div class="select-product-campo">
            <label> Descripcion del producto:  </label>
            <textarea v-model="descripcion" rows="5" readonly></textarea>
        </div>
        <div class="select-product-campo">
            <label> Cantidad de unidades del producto:  </label>
            <input v-model="cantidad" type="text" readonly>
        </div>
        <div class="select-product-campo">
            <label> Precio del producto:  </label>
            <input v-model="precio" type="text" readonly>
        </div>

    </div>
</template>

<script setup>

    import { useStore } from '@/store/pinia';
    import { ref, onMounted } from 'vue'
    import { useRoute } from 'vue-router';

    const pinia = useStore()
    const ruta = useRoute()

    let nombre = ref("")
    let categoria = ref("1")
    let imagen = ref("")
    let descripcion = ref("Descripcion")
    let cantidad = ref(1)
    let precio = ref(1)

    onMounted(() => {

        nombre.value = pinia.listaProductos[ruta.params.id].nombre
        categoria.value = pinia.listaProductos[ruta.params.id].categoria
        imagen.value = pinia.listaProductos[ruta.params.id].img
        descripcion.value = pinia.listaProductos[ruta.params.id].descripcion
        cantidad.value = pinia.listaProductos[ruta.params.id].cantidad
        precio.value = pinia.listaProductos[ruta.params.id].precio

    })

</script>

<style lang="scss" scoped>

    .select-product{

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

            height: 20%;

            div{

                width: 100%;
                height: 100%;
                padding: 20px;

            }

        }

        &-campo:nth-child(5){

            display: flex;
            flex-direction: column;

            textarea{

                resize: none;

            }

        }

    }

</style>