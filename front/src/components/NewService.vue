<template>
    <div class="div-crear-servicio">
        <h1> Agregar servicio </h1>
        <div>
            <label> Nombre del servicio:  </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
        </div>
        <div>
            <label> Imagen del producto:  </label>
            <input type="file" placeholder="Imagen" @change="verImagen">
        </div>
        <div class="contenedor-descripcion">
            <label> Descripcion del servicio:  </label>
            <textarea v-model="descripcion" rows="5"></textarea>
        </div>
        <div>
            <label> Precio del servicio:  </label>
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

    const pinia = useStore()

    const emits = defineEmits(['ocultarInterfaz'])

    let nombre = ref<string>("")
    let imagen = ref<string>("")
    let descripcion = ref<string>("Descripcion")
    let precio = ref<number>(1)

    const limpiar = () => {

        nombre.value = ""
        imagen.value = ""
        descripcion.value = "Descripcion"
        precio.value = 1

    }

    const verImagen = (objeto: any) => imagen.value = objeto.target.files[0]

    const crear = () => {

        const cuerpoFormData = new FormData()

        cuerpoFormData.append('nombre', nombre.value)
        cuerpoFormData.append('img', imagen.value)
        cuerpoFormData.append('descripcion', descripcion.value)
        cuerpoFormData.append('precio', String(precio.value))
    
        fetch("http://127.0.0.1:8000/post/service/", {

            method: 'POST',
            body: cuerpoFormData

        })

        setTimeout(() => {

            pinia.getServicios()
            limpiar()

        }, 500)

    }

    const ocultar = () => emits('ocultarInterfaz')

</script>

<style lang="scss" scoped>

    .div-crear-servicio{

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