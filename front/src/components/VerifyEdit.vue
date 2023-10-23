<template>

    <div class="panel-verify">
    
        <h1> Contraseña de verificacion </h1>
        <p> Para poder continuar necesitamos que verifiques tu contraseña  </p>
        <input type="password" placeholder="***********">
        <button @click="emits('verify')"> Cancelar </button>
        <p> {{ texto }} </p>

    </div>

</template>

<script lang="ts" setup>

    import { ref, defineEmits } from 'vue'

    const emits = defineEmits(['verify'])

    let texto = ref<string>("No dudamos que seas tu, solo son temas de seguridad :)")

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
        align-content: center;
        position: absolute;
        z-index: 1000;

        input{

            @include inputs();

        }

    }

</style>