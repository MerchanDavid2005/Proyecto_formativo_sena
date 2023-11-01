<template>
    <div class="new-category" :style="{background: pinia.fondoEdits}">
        
        <h1 class="new-category-title"> Nueva categoria </h1>
        <p class="error" v-if="error"> No dejes ningun campo en blanco </p>
        <div class="new-category-campo">
            <label> Nombre de la categoria:  </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
        </div>
        <div class="new-category-button">
            <button 

                :style="{background: pinia.fondoRed}" 
                @click="emits('cerrar')"> Cancelar 

            </button>

            <button 

                :style="{background: pinia.greentheme}" 
                @click="cargarDatos"> Crear 

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

    let error = ref(false)

    async function nuevaCategoria(){

        if(nombre.value != ""){

            const peticion = await fetch(`http://127.0.0.1:8000/api/Categoria/`, {

                method: 'POST',
                body: JSON.stringify({

                    nombre: nombre.value

                }),
                headers: {"content-type": "application/json"}

            });

            return peticion

        }else{

            error.value = true
            return "Error"

        }
        
    }

    const cargarDatos = async () => {

        pinia.cargandoDatos = true

        try{

            const respuesta = await nuevaCategoria()

            if(respuesta !== "Error"){

                emits('cerrar')
                pinia.getCategorias()
                nombre.value = ""
                pinia.exitoFetch = true
                setTimeout(() => {

                    pinia.exitoFetch = false

                }, 3000)

            }

            pinia.cargandoDatos = false

        }catch(e){

            pinia.cargandoDatos = false
            pinia.errorFetch = true
            setTimeout(() => {

                pinia.errorFetch = false

            }, 3000)

        }

    } 

</script>

<style lang="scss" scoped>

    .new-category{

        height: 35%;
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

        .error{

            text-align: center;
            color: #f00;
            margin-bottom: 20px;

        }

        &-campo{

            margin-bottom: 10px;

            input{

                @include inputs();

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

    @media(max-width: 1599px){

        .new-category{

            width: 40%;
           
            &-title{

                margin: 20px 0;

            }

        }

    }

    @media(min-width:1600px){

        .new-category{

            height: 25%;

        }

    }

</style>