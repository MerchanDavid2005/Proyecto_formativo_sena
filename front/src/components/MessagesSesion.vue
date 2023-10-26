<template>

    <div class="messages-sesion-none">
        
        <div class="messages-sesion-none-icon">
            <v-icon name="fa-user-times" scale="4"></v-icon>
        </div>
        <div class="messages-sesion-none-text">
            <h1> Sesion caducada </h1>
            <p> Tu inicio de sesion ha cadudado, por favor vuelve a iniciar sesion </p>
        </div>

    </div>

</template>

<style lang="scss" scoped>

    .messages-sesion-none{

        width: 25%;
        height: max-content;
        border-radius: 20px;
        padding: 15px;
        display: flex;
        align-items: center;
        justify-content: space-around;
        position: absolute;
        top: 5%;
        right: 2%;
        z-index: 1000000;
        background: #f05;
        color: #fff;

        &-icon{

            width: 30%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;

        }

        &-text{

            width: 70%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;

        }

    }

</style>