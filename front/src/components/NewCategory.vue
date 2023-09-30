<template>
    <div class="div-crear-producto">
        <h1> Agregar categoria </h1>
        <div>
            <label> Nombre de la categoria:  </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
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
    
    const limpiar = () => {

        nombre.value = ""

    }

    const crear = () => {

        fetch("http://127.0.0.1:8000/api/Categoria/", {

            method: 'POST',
            body: JSON.stringify({

                nombre: nombre.value

            }),
            headers: {"content-type" : "application/json"}

        })

        setTimeout(() => {

            pinia.getCategorias()
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