<template>
    <div class="new-service" :style="{background: pinia.fondoEdits}">
        
        <h1 class="new-service-title"> Nuevo servicio </h1>
        <div class="new-service-campo">
            <label> Nombre del servicio:  </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
        </div>
        <div class="new-service-campo">
            <label> Imagen ilustrativa del producto:  </label>
            <input type="file" :onchange="imagenValor">
        </div>
        <div class="new-service-campo">
            <label> Descripcion del servicio:  </label>
            <textarea v-model="descripcion" rows="5"></textarea>
        </div>
        <div class="new-service-campo">
            <label> Precio del servicio:  </label>
            <input v-model="precio" type="text" placeholder="Precio">
        </div>
        <div class="new-service-button">
            <button 

                :style="{background: pinia.fondoRed}" 
                @click="emits('cerrar')"> Cancelar 

            </button>

            <button 

                :style="{background: pinia.greentheme}" 
                @click="nuevoServicio"> Crear 

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
    let imagen = ref("")
    let descripcion = ref("Descripcion")
    let precio = ref(1)

    const imagenValor = (img) => imagen.value = img.target.files[0]

    function nuevoServicio(){

        let bodyForm = new FormData()

        bodyForm.append('nombre', nombre.value)
        bodyForm.append("img", imagen.value)
        bodyForm.append('descripcion', descripcion.value)
        bodyForm.append('precio', precio.value)

        fetch(`http://127.0.0.1:8000/post/service/`, {

            method: 'POST',
            body: bodyForm

        });

        emits('cerrar')

        setTimeout(() => {

            pinia.getServicios()
            nombre.value = ""
            imagen.value = ""
            descripcion.value = "Descripcion"
            precio.value = 1

        }, 600)
        
    }

</script>

<style lang="scss" scoped>

    .new-service{

        height: 75%;
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

        &-campo{

            margin-bottom: 10px;

            input, textarea{

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
            justify-content: space-between;
            align-items: flex-end;

            button{

                @include botones();
                height: max-content;

            }

        }

    }

</style>