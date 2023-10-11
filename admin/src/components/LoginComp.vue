<template>

    <div class="cuerpo-login">
        
        <h1 class="cuerpo-login-titulo"> Iniciar sesion </h1>
        <p class="cuerpo-login-campo-text"> Ingresa tu nombre de usuario </p>
        <input type="text" placeholder="Usuario">
        <p class="cuerpo-login-campo-text"> Ingresa tu contraseña </p>
        <input type="password" placeholder="Contraseña">
        <p class="cuerpo-login-mensaje"> ¿Aun no tienes una cuenta?  </p>
        <p class="cuerpo-login-mensaje"> 
            Puedes registrarte siguiendo el siguien enlace 
            <router-link to="/register"> registrarse </router-link>
        </p>
        <button> Iniciar sesion </button>

    </div>

</template>

<style lang="scss" scoped>

    .cuerpo-login{

        height: 45%;
        width: 25%;
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