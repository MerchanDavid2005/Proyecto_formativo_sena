<template>

    <div class="cuerpo-login">
        
        <h1 class="cuerpo-login-titulo"> Iniciar sesion </h1>
        <p class="cuerpo-login-campo-text"> Ingresa tu nombre de usuario </p>
        <input v-model="usuario" type="text" placeholder="Usuario">
        <p class="cuerpo-login-campo-text"> Ingresa tu contraseña </p>
        <input v-model="password" type="password" placeholder="Contraseña">
        <p class="cuerpo-login-mensaje"> ¿Aun no tienes una cuenta?  </p>
        <p class="cuerpo-login-mensaje"> 
            Puedes registrarte siguiendo el siguien enlace 
            <router-link to="/register"> registrarse </router-link>
        </p>
        <button @click="iniciarSesion"> Iniciar sesion </button>

    </div>

</template>

<script setup>

    import { ref } from 'vue';
    import { useRouter } from 'vue-router';

    const enrutado = useRouter();

    let usuario = ref("");
    let password = ref("");

    function iniciarSesion(){

        fetch("http://localhost:8000/login/", {

            method: 'POST',
            body: JSON.stringify({

                usuario: usuario.value,
                password: password.value 

            }),
            headers: {"content-type": "application/json"}

            }).then(res => res.json()).then(info => {

            localStorage.setItem('token', JSON.stringify({"token": info.token}))

        });

        
        if(localStorage.getItem('token') != "error" && localStorage.getItem("token") !== null){

            enrutado.push('/admin/product');

        }

    }

    if(localStorage.getItem('token') != "error" && localStorage.getItem("token") !== null){

        enrutado.push('/admin/product');

    }

</script>

<style lang="scss" scoped>

    .cuerpo-login{

        height: 65%;
        width: 30%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 15px;
        border-radius: 15px;
        position: static;
        z-index: 100;
        background: #fff;

        &-titulo{

            margin: 20px 0;
            align-self: center;

        }

        input{

            @include inputs();
            margin: 10px 0;
            width: 100%;

        }

        button{

            @include botones();
            background: $second-color;
            width: max-content;
            align-self: center;
            margin: 10px 0;

        }

        &-mensaje{

            align-self: center;
            margin: 10px 0;
            font-size: 15px;

        }

    }

</style>