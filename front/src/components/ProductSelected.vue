<template>
    <article class="product-selected">
        <h1> Producto sin editar </h1>
        <div>
            <label> Nombre del producto: </label>
            <input type="text" :value="nombre" readonly>
        </div>
        <div>
            <label> Categoria del producto: </label>
            <input type="text" :value="categoria" readonly>
        </div>
        <div class="imagen-producto">
            <img :src="imagen" :alt="`Producto: ${nombre}`">
        </div>
        <div class="contenedor-descripcion">
            <label> Descripcion del producto: </label>
            <textarea v-model="descripcion" rows="5" readonly> </textarea>
        </div>
        <div>
            <label> Cantidad de unidades del producto: </label>
            <input type="number" :value="cantidad" readonly>
        </div>
        <div>
            <label> Precio por unidad del producto: </label>
            <input type="number" :value="precio" readonly>
        </div>
    </article>
</template>

<script lang="ts" setup>

    import { useRoute } from 'vue-router';
    import { onMounted, ref } from 'vue';

    const route = useRoute()

    let nombre = ref<string>("")
    let descripcion = ref<string>("")
    let imagen = ref<string>("")
    let categoria = ref<string>("")
    let cantidad = ref<number>(1)
    let precio = ref<number>(1)

    onMounted(() => {

        fetch(`http://127.0.0.1:8000/get/product/${route.params.id}/`)
            .then(res => res.json())
            .then(info => {

                nombre.value = info.producto.nombre
                descripcion.value = info.producto.descripcion
                imagen.value = info.producto.img
                categoria.value = info.producto.categoria
                cantidad.value = info.producto.cantidad
                precio.value = info.producto.precio

            })

    })

</script>

<style lang="scss" scoped>

    .product-selected{

        width: 30%;
        height: 90%;
        padding: 15px;
        background: #fff;
        outline: 2px solid #000;
        border-radius: 10px;

        h1{

            text-align: center;
            margin: 20px 0;
            font-size: 25px;

        }

        div{

            margin: 10px 0;

            input, select, textarea{

                @include inputs();
    
            }
    

        }

        .imagen-producto{

            width: 100%;
            height: 20%;
            padding: 10px;
            box-sizing: border-box;

        }

        .contenedor-descripcion{

            display: flex;
            flex-direction: column;

        }


    }

</style>

