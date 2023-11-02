<template>

    <div class="error-load">
        
        <v-icon name="md-error" scale="5"></v-icon>
        <h1> Error </h1>
        <p> Ha habido un error al cargar la pagina </p>
        <button> Volver a intentar </button>

    </div>

</template>

<style lang="scss" scoped>

    .error-load{

        width: 40%;
        height: max-content;
        padding: 20px;
        border-radius: 30px;
        display: flex;
        flex-direction: column;
        align-items: center;
        background: $fondo-input;
        color: #000;

    }

</style>