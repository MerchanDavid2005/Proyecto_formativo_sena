<template>
    <div class="confirm-delete">
        
        <div class="confirm-delete-data">
            <div class="confirm-delete-data-icon">
                <v-icon name="md-deleteforever" scale="5"></v-icon>
            </div>
            <div class="confirm-delete-data-msg">
                <h1> Eliminar </h1>
                <p> ¿Estas seguro de querer eliminar {{ props.registro }}? </p>
            </div>
        </div>
        <div class="confirm-delete-buttons">
            <button @click="eliminar"> Si, aceptar </button>
            <button @click="emits('cerrar')"> No, cancelar </button>
        </div>

    </div>
</template>

<script setup>

    import { defineProps, defineEmits } from 'vue';
    import { useStore } from '@/store/pinia' 

    const pinia = useStore()
    const emits = defineEmits(['cerrar'])
    const props = defineProps(['modelo', 'registro'])

    function eliminar(){

        pinia.eliminar(props.modelo)
        emits('cerrar')

        setTimeout(() => {

            pinia.getProductos()

        }, 600)

    }

</script>

<style lang="scss" scoped>

    .confirm-delete{

        width: 30%;
        height: 30%;
        padding: 2%;
        display: flex;
        flex-direction: column;
        background: $third-color;
        border-radius: 15px;
        position: absolute;
        z-index: 10000;

        &-data{

            width: 100%;
            height: 65%;
            display: flex;
            margin-bottom: 20px;

            &-icon{

                height: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                width: 30%;
                color: #fff;

            }

            &-msg{

                color: #fff;
                display: flex;
                flex-direction: column;
                justify-content: space-around;
                align-items: center;

            }

        }

        &-buttons{

            button:nth-child(1){

                @include botones();
                background: $forth-color;
                margin-right: 10px;
                color: #000;
                font-weight: 100;

            }

            button:nth-child(2){

                @include botones();
                background: $forth-color;
                color: #000;
                font-weight: 100;

            }

        }

    }

</style>