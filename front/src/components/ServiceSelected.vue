<template>
    <article class="service-selected">
        <h1> Servicio sin editar </h1>
        <div>
            <label> Nombre del servicio: </label>
            <input type="text" :value="nombre" readonly>
        </div>
        <div class="imagen-producto">
            <img :src="imagen" :alt="`Producto: ${nombre}`">
        </div>
        <div class="contenedor-descripcion">
            <label> Descripcion del servicio: </label>
            <textarea v-model="descripcion" rows="5" readonly> </textarea>
        </div>
        <div>
            <label> Precio por el servicio: </label>
            <input type="number" :value="precio" readonly>
        </div>
    </article>
</template>

<script lang="ts" setup>

    import { useRoute } from 'vue-router';
    import { onMounted, ref } from 'vue';

    const route = useRoute()

    let nombre = ref<string>("")
    let imagen = ref<string>("")
    let descripcion = ref<string>("")
    let precio = ref<number>(1)

    onMounted(() => {

        fetch(`http://127.0.0.1:8000/api/Servicio/${route.params.id}/`)
            .then(res => res.json())
            .then(info => {

                nombre.value = info.nombre
                imagen.value = info.img
                descripcion.value = info.descripcion
                precio.value = info.precio

            })

    })

</script>

<style lang="scss" scoped>

    .service-selected{

        width: 30%;
        height: 80%;
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
            height: 35%;
            padding: 10px;
            box-sizing: border-box;

        }

        .contenedor-descripcion{

            display: flex;
            flex-direction: column;

        }


    }

</style>

