<template>

    <div class="error-load-comp">
        
        <v-icon name="md-error" scale="7"></v-icon>
        <h1> Error </h1>
        <p> El servidor esta caido, por favor vuelve a ingresar mas tarde </p>

    </div>

</template>

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