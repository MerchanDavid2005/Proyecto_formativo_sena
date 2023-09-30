<template>
    <article class="product-selected">
        <h1> Editar producto </h1>
        <div>
            <label> Nombre del producto: </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
        </div>
        <div>
            <label> Categoria del producto: </label>
            <select v-model="categoria">
                <option v-for="(cate, i) in pinia.listaCategorias" :key="i" :value="cate.id">
                    {{ cate.nombre }}
                </option>
            </select>
        </div>
        <div>
            <label> Imagen del producto:  </label>
            <input type="file" placeholder="Imagen" @change="verImagen">
        </div>
        <div class="contenedor-descripcion">
            <label> Descripcion del producto: </label>
            <textarea v-model="descripcion" rows="5"></textarea>
        </div>
        <div>
            <label> Cantidad de unidades del producto: </label>
            <input v-model="cantidad" type="number" placeholder="Cantidad">
        </div>
        <div>
            <label> Precio por unidad del producto: </label>
            <input v-model="precio" type="number" placeholder="Precio">
        </div>
        <div class="contenedor-botones">
            <button @click="limpiar"> Limpiar </button>
            <router-link class="boton-actualizar" :to="{name: 'datos'}">
                <button @click="actualizar"> Actualizar </button>
            </router-link>
        </div>
    </article>
</template>

<script lang="ts" setup>

    import { useRoute } from 'vue-router';
    import { useStore } from '../store/pinia';
    import { ref } from 'vue';

    const pinia = useStore()
    const route = useRoute()

    let nombre = ref<string>("")
    let descripcion = ref<string>("Descripcion")
    let imagen = ref<string>("")
    let categoria = ref<string>("1")
    let cantidad = ref<number>(1)
    let precio = ref<number>(1)

    const verImagen = (objeto: any) => imagen.value = objeto.target.files[0]

    const limpiar = () => {

        nombre.value = ""
        descripcion.value = "Descripcion"
        imagen.value = ""
        categoria.value = "1"
        cantidad.value = 1
        precio.value = 1

    }

    const actualizar = () => {

        const formDataImg = new FormData()
        formDataImg.append('img', imagen.value)

        fetch(`http://127.0.0.1:8000/put/product/img/${route.params.id}/`, {

            method: 'POST',
            body: formDataImg
            
        });

        fetch(`http://127.0.0.1:8000/api/Producto/${route.params.id}/`, {

            method: 'PATCH',
            body: JSON.stringify({

                nombre: nombre.value,
                descripcion: descripcion.value,
                categoria: categoria.value,
                cantidad: cantidad.value,
                precio: precio.value

            }),
            headers: {"content-type" : "application/json"}

        });

        setTimeout(() => {

            pinia.getProductos()
            limpiar()

        }, 500)

    }

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
        .contenedor-descripcion{

            display: flex;
            flex-direction: column;

        }

        .contenedor-botones{

            display: flex;
            justify-content: space-evenly;
            margin: 5vh 0;

            button{

                @include botones($fondo-boton-limpiar);
                width: 40%;

            }

            .boton-actualizar{

                width: 40%;
                text-decoration: none;
                color: #fff;

                button{

                    @include botones($fondo-boton-crear);
                    width: 100%;

                }

            }

        }

    }

</style>

