<template>
    <div class="edit-service">
        
        <h1 class="edit-service-title"> Editar servicio </h1>
        <div class="edit-service-campo">
            <label> Nombre del servicio:  </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
        </div>
        <div class="edit-service-campo">
            <label> Imagen ilustrativa del servicio:  </label>
            <input type="file" :onchange="imagenValor">
        </div>
        <div class="edit-service-campo">
            <label> Descripcion del servicio:  </label>
            <textarea v-model="descripcion" rows="5"></textarea>
        </div>
        <div class="edit-service-campo">
            <label> Precio del servicio:  </label>
            <input v-model="precio" type="text" placeholder="Precio">
        </div>
        <div class="edit-service-button">
            <button @click="editarServicio"> Editar </button>
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

    const imagenValor = (img) => imagen.value = img.target.files[0]

    function editarServicio(){

        let servicio = pinia.listaServicios[ruta.params.id]

        fetch(`http://127.0.0.1:8000/api/Servicio/${servicio.id}/`, {

            method: 'PATCH',
            body: JSON.stringify({

                nombre: nombre.value,
                descripcion: descripcion.value,
                precio: precio.value

            }),
            headers: {"content-type": "application/json"}

        });

        let bodyForm = new FormData()
        bodyForm.append("img", imagen.value)

        fetch(`http://127.0.0.1:8000/put/service/img/${servicio.id}/`, {

            method: 'POST',
            body: bodyForm

        });

        enrutado.push('/admin/service')

        setTimeout(() => {

            pinia.getServicios()

        }, 600)

    }

</script>

<style lang="scss" scoped>

    .edit-service{

        height: 75%;
        width: 30%;
        display: flex;
        flex-direction: column;
        outline: 2px solid #000;
        border-radius: 15px;
        padding: 15px;

        &-title{

            text-align: center;
            margin: 40px;

        }

        &-campo{

            margin-bottom: 40px;

            input, textarea, select{

                @include inputs();

            }

        }

        &-campo:nth-child(3){

            display: flex;
            flex-direction: column;

            input{

                margin: 10px 0;

            }

        }

        &-campo:nth-child(4){

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
            justify-content: flex-end;
            align-items: flex-end;

            button{

                @include botones($first-color);
                height: max-content;

            }

        }

    }

</style>