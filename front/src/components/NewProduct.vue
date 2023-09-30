<template>
    <div class="div-crear-producto">
        <h1> Agregar producto </h1>
        <div>
            <label> Nombre del producto:  </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
        </div>
        <div>
            <label> Categoria del producto:  </label>
            <select v-model="categoria">
                <option 
                    v-for="(cate, i) in pinia.listaCategorias" :key="i" 
                    :value="cate.id"> {{ cate.nombre }} 
                </option>
            </select>
        </div>
        <div>
            <label> Imagen del producto:  </label>
            <input type="file" placeholder="Imagen" @change="verImagen">
        </div>
        <div class="contenedor-descripcion">
            <label> Descripcion del producto:  </label>
            <textarea v-model="descripcion" rows="5"></textarea>
        </div>
        <div>
            <label> Cantidad del producto:  </label>
            <input v-model="cantidad" type="number" placeholder="Cantidad">
        </div>
        <div>
            <label> Precio por unidad del producto:  </label>
            <input v-model="precio" type="number" placeholder="Precio">
        </div>
        <div class="contenedor-botones">
            <div>
                <button @click="ocultar"> Cerrar </button>
            </div>
            <div>
                <button @click="limpiar"> Limpiar </button>
                <button @click="crear"> Crear </button>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia';

    import { ref, defineEmits } from 'vue';

    const emits = defineEmits(['ocultarInterfaz'])

    const pinia = useStore()

    let nombre = ref<string>("")
    let categoria = ref<string>("1")
    let descripcion = ref<string>("Descripcion")
    let imagen = ref<string>("")
    let cantidad = ref<number>(1)
    let precio = ref<number>(1)

    const verImagen = (objeto: any) => imagen.value = objeto.target.files[0]

    const limpiar = () => {

        nombre.value = ""
        categoria.value = "1"
        descripcion.value = "Descripcion"
        cantidad.value = 1
        precio.value = 1

    }

    const crear = () => {

        const cuerpoData = new FormData()
        
        cuerpoData.append('nombre', nombre.value);
        cuerpoData.append('categoria', categoria.value);
        cuerpoData.append('img', imagen.value);
        cuerpoData.append('descripcion', descripcion.value);
        cuerpoData.append('cantidad', String(cantidad.value));
        cuerpoData.append('precio', String(precio.value));

        fetch("http://127.0.0.1:8000/post/product/", {

            method: 'POST',
            body: cuerpoData

        })

        setTimeout(() => {

            pinia.getProductos()
            limpiar()

        }, 500)

    }

    const ocultar = () => emits('ocultarInterfaz')

</script>

<style lang="scss" scoped>

    .div-crear-producto{

        position: absolute;
        z-index: 1000;
        width: 30%;
        padding: 15px;
        background: #fff;
        outline: 2px solid #000;
        border-radius: 10px;

        h1{

            text-align: center;
            margin: 20px 0;

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
            justify-content: space-between;

            div:nth-child(1){

                button{

                    @include botones($fondo-boton-eliminar);

                }

            }

            div:nth-child(2){

                button:nth-child(1){

                    @include botones($fondo-boton-limpiar)

                }

                button:nth-child(2){

                    @include botones($fondo-boton-crear);
                    margin-left: 10px;

                }

            }

        }

    }

</style>