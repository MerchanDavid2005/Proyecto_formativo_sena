<template>

    <div class="form-login">
        
        <h1> Iniciar sesion </h1>
        <label> Nombre de usuario: </label>
        <input type="text" placeholder="Usuario">
        <label> Contraseña:  </label>
        <input type="password" placeholder="**********">
        <p> ¿Aun no tienes una cuenta? </p>
        <p> Puedes registrarte siguien el siguiente enlace <router-link to="/registrar"> registrarse </router-link> </p>
        <button> Iniciar sesion </button>

    </div>

</template>

<style lang="scss">

    .form-login{

        width: 25%;
        height: 45%;
        display: flex;
        flex-direction: column;
        align-items: center;
        position: static;
        z-index: 1000;
        background: #fff;
        border-radius: 15px;
        padding: 15px;

        h1{

            margin: 20px 0 45px 0;
            font-size: 40px;

        }

        label{

            align-self: flex-start;
            margin: 5px 0;

        }

        input{

            @include inputs();
            width: 100%;
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

</style>
