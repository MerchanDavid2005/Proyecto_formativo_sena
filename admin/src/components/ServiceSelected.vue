<template>
    <div class="select-service">
        
        <h1 class="select-service-title"> Servicio sin editar </h1>
        <div class="select-service-campo">
            <label> Nombre del servicio:  </label>
            <input v-model="nombre" type="text" readonly>
        </div>
        <div class="select-service-campo">
            <label> Imagen ilustrativa del servicio:  </label>
            <div>
                <img :src="imagen" :alt="nombre">
            </div>
        </div>
        <div class="select-service-campo">
            <label> Descripcion del servicio:  </label>
            <textarea v-model="descripcion" rows="5" readonly></textarea>
        </div>
        <div class="select-service-campo">
            <label> Precio del servicio:  </label>
            <input v-model="precio" type="text" readonly>
        </div>

    </div>
</template>

<script setup>

    import { useStore } from '@/store/pinia';
    import { ref, onMounted } from 'vue'
    import { useRoute } from 'vue-router';

    const pinia = useStore()
    const ruta = useRoute()

    let nombre = ref("")
    let imagen = ref("")
    let descripcion = ref("Descripcion")
    let precio = ref(1)

    onMounted(() => {

        nombre.value = pinia.listaServicios[ruta.params.id].nombre
        imagen.value = pinia.listaServicios[ruta.params.id].img
        descripcion.value = pinia.listaServicios[ruta.params.id].descripcion
        precio.value = pinia.listaServicios[ruta.params.id].precio

    })

</script>

<style lang="scss" scoped>

    .select-service{

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

            margin-bottom: 20px;

            input, textarea, select{

                @include inputs();

            }

        }

        &-campo:nth-child(3){

            height: 35%;

            div{

                width: 100%;
                height: 100%;
                padding: 20px;

            }

        }

        &-campo:nth-child(4){

            display: flex;
            flex-direction: column;

            textarea{

                resize: none;

            }

        }

    }

</style>