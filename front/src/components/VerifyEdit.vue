<template>

    <div class="panel-verify">
    
        <h1> Contraseña de verificacion </h1>
        <p class="panel-verify-error" v-if="error"> La contraseña ingresada es incorrecta </p>
        <p> Para poder continuar necesitamos que verifiques tu contraseña  </p>
        <input v-model="contra" type="password" placeholder="***********">
        <button @click="recargarDatos" class="panel-verify-boton-aceptar"> Aceptar </button>
        <button class="panel-verify-boton-cancelar" @click="emits('ocultar')"> Cancelar </button>
        <p> {{ texto }} </p>

    </div>

</template>

<script lang="ts" setup>

    import { ref, defineEmits } from 'vue'
    import { useStore } from '../store/pinia';

    const pinia = useStore()
    const emits = defineEmits(['ocultar'])

    let contra = ref<string>("")
    let texto = ref<string>("No dudamos que seas tu, solo son temas de seguridad :)")
    let error = ref<boolean>(false)

    async function actualizarDatos(){

        if(contra.value == pinia.datosUsuario.password){

            let datosUsuario = new FormData()

            datosUsuario.append("password", contra.value)
            datosUsuario.append("usuario", pinia.datosUsuarioEditar.nombre_usuario)
            datosUsuario.append("nombre", pinia.datosUsuarioEditar.nombre)
            datosUsuario.append("email", pinia.datosUsuarioEditar.email)
            datosUsuario.append("img", pinia.datosUsuarioEditar.foto)

            const data = await fetch(`http://localhost:8000/put/user/${pinia.datosUsuario.id}/`, {

                method: 'POST',
                body: datosUsuario

            })

            return data.json()

        }else{

            error.value = true

        }

    }

    async function recargarDatos(){

        const estado = await actualizarDatos()

        if(estado.Mensaje == "¡Actualizado!"){

            pinia.getUsuario(pinia.datosUsuario.id);
            emits('ocultar')

        }else{

            error.value = true

        }

    }

</script>

<style lang="scss" scoped>

    .panel-verify{

        width: 40%;
        height: max-content;
        padding: 15px;
        border-radius: 15px;
        display: flex;
        flex-direction: column;
        justify-content: space-evenly;
        align-items: center;
        position: absolute;
        z-index: 1000;
        background: #fff;

        h1{

            margin: 15px 0

        }

        &-error{

            text-align: center;
            margin: 10px 0;
            color: #f00

        }

        input{

            @include inputs();
            margin: 10px 0;
            text-align: center;
            width: 40%

        }

        &-boton-aceptar{

            @include botones($fondo-boton-crear);
            width: 40%;
            margin: 10px 0;

        }

        &-boton-cancelar{

            @include botones($fondo-boton-eliminar);
            width: 40%;
            margin: 10px 0;

        }

        p{

            margin: 10px 0;

        }

    }

</style>