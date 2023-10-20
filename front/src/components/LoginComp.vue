<template>

    <div class="form-login">
        
        <h1> Iniciar sesion </h1>
        <p v-if="errorCredenciales" class="error"> Los datos ingresados son incorrectos </p>
        <label> Nombre de usuario: </label>
        <input v-model="usuario" type="text" placeholder="Usuario">
        <label> Contraseña:  </label>
        <input v-model="password" type="password" placeholder="**********">
        <p> ¿Aun no tienes una cuenta? </p>
        <p> Registrate en el siguiente enlace <router-link to="/registrar"> registrarse </router-link> </p>
        <button @click="entrar"> Iniciar sesion </button>

    </div>

</template>

<script lang="ts" setup>

    import { ref } from 'vue';
    import { useRouter } from 'vue-router';
    import { useStore } from '../store/pinia';
    import jwt_decode from 'jwt-decode'

    const pinia = useStore()
    const enrutado = useRouter();

    let usuario = ref<string>("");
    let password = ref<string>("");
    let errorCredenciales = ref(false);

    type infoToken = {

        id: number,
        exp: string

    }

    async function verificarDatos(){

        const data = await fetch("http://localhost:8000/login/Cliente/", {

            method: 'POST',
            body: JSON.stringify({

                usuario: usuario.value,
                password: password.value 

            }),
            headers: {"content-type": "application/json"}

        });

        return data.json()

    }

    async function entrar(){

        let informacion = await verificarDatos()

        if(informacion.token == "Error"){

            errorCredenciales.value = true

        }else{

            localStorage.setItem("token", JSON.stringify({"token": informacion.token}))
            const tokenDecodificado: infoToken = jwt_decode(informacion.token);
            pinia.usuarioLogeado = true
            pinia.usuario = tokenDecodificado.id
            pinia.getUsuario(tokenDecodificado.id)
            enrutado.push("/")

        }

    }

    if(localStorage.getItem("token") != null){

        enrutado.push('/')

    }

</script>

<style lang="scss" scoped>

    .form-login{

        width: 25%;
        height: 60%;
        display: flex;
        flex-direction: column;
        justify-content: space-evenly;
        align-items: center;
        position: static;
        z-index: 1000;
        background: #fff;
        border-radius: 15px;
        padding: 25px;

        h1{

            margin: 25px 0;
            font-size: 40px;

        }
        
        .error{

            text-align: center;
            color: #f00;
            margin-bottom: 20px;

        }

        label{

            align-self: flex-start;

        }

        input{

            align-self: flex-start;
            @include inputs();
            width: 95%;
            height: max-content;
            margin: 10px 0;

        }

        p{

            margin: 10px 0;

        }

        button{

            @include botones($fondo-boton-limpiar);
            height: max-content;
            width: max-content;
            margin-top: 20px;

        }

    }

    @media(min-width:1600px){

        .form-login{

            width: 20%;
            height: 45%;

            button{

                margin-top: 20px;
    
            }

        }

    }

</style>
