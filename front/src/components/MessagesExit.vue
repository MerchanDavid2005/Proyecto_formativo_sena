<template>

    <div class="messages-buy">
        
        <div class="messages-buy-icon">
            <v-icon name="bi-check" scale="4"></v-icon>
        </div>
        <div class="messages-buy-text">
            <h1> Pedido realizado </h1>
            <p> El pedido se ha realizado exitosamente </p>
        </div>

    </div>

</template>

<style lang="scss" scoped>

    .messages-buy{

        width: 30%;
        height: max-content;
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        padding: 15px;
        border-radius: 20px;
        background: $fondo-boton-crear;
        color: #fff;
        position: absolute;
        top: 5%;
        right: 2%;
        z-index: 100000;

        &-icon{

            width: max-content;

        }

        &-text{

            display: flex;
            flex-direction: column;
            justify-content: space-evenly;

            h1{

                font-size: 25px;

            }

            p{

                font-size: 20px;

            }

        }

    }

    @media (min-width:1600px){

        .messages-buy{

            width: 25%;

        }

    }

</style>