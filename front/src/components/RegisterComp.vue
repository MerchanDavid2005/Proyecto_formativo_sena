<template>

    <div class="form-register">
        
        <h1> Registrarse </h1>
        <p v-if="error" class="error"> Los datos ingresados son incorrectos </p>
        <div class="form-register-row">
            <div class="form-register-row-column">
                <label> Nombre de usuario: </label>
                <input v-model="usuario" type="text" placeholder="Usuario">
            </div>
            <div class="form-register-row-column">
                <label> Nombre: </label>
                <input v-model="nombre" type="text" placeholder="Nombre">
            </div>
        </div>
        <div class="form-register-correo">
            <label> Correo: </label>
            <input v-model="correo" type="text" placeholder="Correo">
        </div>
        <div class="form-register-avatar">
            <label> Avatar (opcional): </label>
            <input type="file" :onchange="valorAvatar">
        </div>
        <div class="form-register-row">
            <div class="form-register-row-column">
                <label> Contraseña: </label>
                <input v-model="contraseña" type="password" placeholder="**********">
            </div>
            <div class="form-register-row-column">
                <label> Verificar contraseña:  </label>
                <input v-model="contraseñaVerificar" type="password" placeholder="**********">
            </div>
        </div>
        <p> ¿Ya tienes una cuenta? </p>
        <p> Inicia sesion en el siguiente enlace <router-link to="/iniciar_sesion"> iniciar sesion </router-link> </p>
        <button @click="registrar"> Registrarse </button>

    </div>

</template>

<script lang="ts" setup>

    import { ref, defineEmits } from 'vue'
    import { useStore } from '../store/pinia';

    const emits = defineEmits(['verificar'])
    const pinia = useStore()

    let nombre = ref<string>("")
    let usuario = ref<string>("")
    let correo = ref<string>("")
    let avatar = ref<string>("")
    let contraseña = ref<string>("")
    let contraseñaVerificar = ref<string>("")

    let error = ref<boolean>(false)
    let mensajeError = ref<string>("")

    const valorAvatar = (img: any) => avatar.value = img.target.files[0]

    function validar(){

        let validado = false

        if(nombre.value != "" && usuario.value != "" && correo.value != "" && contraseña.value != "" && contraseñaVerificar.value != ""){

            if(contraseña.value == contraseñaVerificar.value){

                validado = true

            }else{

                error.value = true
                mensajeError.value = "Las contraseñas no coinciden"

            }

        }else{

            error.value = true
            mensajeError.value = "No dejes campos en blanco"

        }

        return validado

    }

    async function registrar(){

        if(validar()){

            fetch("http://localhost:8000/send/code/verify/", {

                method: 'POST',
                body: JSON.stringify({

                    usuario: usuario.value,
                    email: correo.value

                }),
                headers: {"content-type": "application/json"}

            }).then(res => res.json()).then(info => {

                pinia.codigoVerificacion = info.Codigo
                
            })

            pinia.datosUsuarioCrear = {

                "usuario": usuario.value,
                "nombre": nombre.value,
                "img": avatar.value,
                "correo": correo.value,
                "password": contraseña.value 

            };

            emits('verificar')

        }

    }

</script>

<style lang="scss">

    .form-register{

        width: 40%;
        height: 75%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: static;
        z-index: 1000;
        background: #fff;
        border-radius: 15px;
        padding: 25px;

        h1{

            margin: 15px 0;
            font-size: 40px;
            text-align: center;

        }

        .error{

            text-align: center;
            color: #f00;
            margin: 10px 0;

        }

        input, select{

            @include inputs();
            width: 100%;

        }

        &-correo{

            width: 95%;
            height: max-content;

        }

        &-avatar{

            width: 95%;
            height: max-content;

        }

        &-row{

            width: 95%;
            height: max-content;
            display: flex;
            justify-content: space-between;

            &-column{

                width: 45%;
                height: max-content;
                display: flex;
                flex-direction: column;

            }

        }

        p{

            text-align: center

        }

        button{

            @include botones($fondo-boton-limpiar);
            height: max-content;
            width: 30%;
            margin-top: 20px;
            align-self: center;

        }

    }

    @media(min-width:1600px){

        .form-register{

            width: 30%;
            height: 75%;

            button{
                
                margin-top: 20px;
    
            }

        }

    }

</style>
