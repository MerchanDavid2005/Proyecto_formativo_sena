<template>

    <div class="error-load-comp">
        
        <v-icon name="md-error" scale="7"></v-icon>
        <h1> Error </h1>
        <p> El servidor esta caido, por favor vuelve a ingresar mas tarde </p>
        <button @click="volverAIntentar"> Volver a intentar </button>

    </div>

</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia'
    import { useRouter } from 'vue-router'

    const pinia = useStore()
    const enrutado = useRouter()

    const volverAIntentar = async () => {

        enrutado.push('/')
        pinia.pantallaCarga = true
        const respuesta = await pinia.cargarDatos();
        
        if(respuesta == "Exito"){

            pinia.pantallaCarga = false
            sessionStorage.setItem("error", "false")

        }else{

            pinia.pantallaCarga = false
            sessionStorage.setItem("error", "true")
            enrutado.push('/error')

        }

    }

</script>

<style lang="scss" scoped>

    .error-load-comp{

        width: 40%;
        height: max-content;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: #fff;

        h1{

            margin: 10px 0;

        }

        p{

            margin: 20px 0;

        }

        button{

            @include botones($fondo-boton-limpiar);
            color: #fff;

        }

    }

</style>