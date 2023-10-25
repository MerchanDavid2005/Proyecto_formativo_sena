<template>
    <div class="edit-service" :style="{background: pinia.fondoEdits}">
        
        <h1 class="edit-service-title"> Editar servicio </h1>
        <p class="error" v-if="error"> {{ mensajeError }} </p>
        <div class="edit-service-campo">
            <label> Nombre del servicio:  </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
        </div>
        <p> Si dejas el campo imagen vacio este tomara la imagen ya existente </p>
        <div class="edit-service-campo-selector">
            <label> Imagen ilustrativa del servicio:  </label>
            <input type="file" :onchange="imagenValor">
        </div>
        <div class="edit-service-campo-descripcion">
            <label> Descripcion del servicio:  </label>
            <textarea v-model="descripcion" rows="5"></textarea>
        </div>
        <div class="edit-service-campo">
            <label> Precio del servicio:  </label>
            <input v-model="precio" type="text" placeholder="Precio">
        </div>
        <div class="edit-service-button">
            <button :style="{background: pinia.greentheme}" @click="editarServicio"> Editar </button>
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
    let imagen = ref("")
    let descripcion = ref("Descripcion")
    let precio = ref(1)

    let error = ref(false)
    let mensajeError = ref("")

    const imagenValor = (img) => imagen.value = img.target.files[0]

    
    function validar(){

        let validado = false

        if(nombre.value != ""  && descripcion.value != "" && precio.value != ""){

            if(imagen.value != ""){

                if(imagen.value.name.toLowerCase().endsWith(".png") || 
                imagen.value.name.toLowerCase().endsWith(".jpg") || 
                imagen.value.name.toLowerCase().endsWith(".jpeg")){

                    validado = true

                }else{

                    error.value = true
                    mensajeError.value = "Solo se permiten archivos con extension png, jpg o jpeg"

                }

            }else{

                validado = true

            }

        }else{

            error.value = true
            mensajeError.value = "No dejes ningun campo en blanco"

        }

        return validado

    }

    async function editarData(){

        let servicio = pinia.listaServicios[ruta.params.id]

        if(validar()){

            const data = await fetch(`http://127.0.0.1:8000/api/Servicio/${servicio.id}/`, {

                method: 'PATCH',
                body: JSON.stringify({

                    nombre: nombre.value,
                    descripcion: descripcion.value,
                    precio: precio.value

                }),
                headers: {"content-type": "application/json"}

            });

            return data

        }

    }

    async function editarImagen(){

        let servicio = pinia.listaServicios[ruta.params.id]

        if(imagen.value != ""){

            let bodyForm = new FormData()
            bodyForm.append("img", imagen.value)

            const data = await fetch(`http://127.0.0.1:8000/put/service/img/${servicio.id}/`, {

                method: 'POST',
                body: bodyForm

            });
            
            return  data

        }else{

            return "No se ha cargado ninguna imagen"

        }

    }

    async function editarServicio(){

        await editarData()
        await editarImagen()

        pinia.getServicios()
        enrutado.push('/admin/service')

    }

</script>

<style lang="scss" scoped>

    .edit-service{

        height: 80%;
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

        .error{

            text-align: center;
            color: #f00;
            margin-bottom: 20px;

        }

        p{

            margin: 15px 0;
            color: #000;
            text-align: center;
            background: #ff0;
            border-radius: 15px;
            padding: 5px;

        }

        &-campo{

            margin-bottom: 10px;

            input, textarea, select{

                @include inputs();

            }

        }

        &-campo-selector{

            display: flex;
            flex-direction: column;

            input{

                @include inputs();
                margin: 10px 0;
                color: #000;

            }

        }

        &-campo-descripcion{

            display: flex;
            flex-direction: column;

            textarea{

                @include inputs();
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

    @media(min-width:1600px){

        .edit-service{

            height: 70%;
            width: 30%;

        }

    }

</style>