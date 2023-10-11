<template>

    <div class="panel-code">
        
        <h1> Codigo de verificacion </h1>
        <p> Se ha enviado un codigo de verificacion al email introducido, por favor ingresa el codigo enviado </p>
        <input v-model="code" type="text" placeholder="XXXXXX" maxlength="6">

    </div>

</template>

<script setup>

    import { ref, watch } from 'vue'
    import { useStore } from '@/store/pinia';
    import { useRouter } from 'vue-router';

    const enrutado = useRouter()
    const pinia = useStore()

    let code = ref("")

    watch(code, () => {

        if(code.value == pinia.codigoVerificacion){

            enrutado.push('/')

            setTimeout(() => {
                
                pinia.mensajeUsuarioRegistrado = true

            }, 1000);

        }

    })

</script>

<style lang="scss" scoped>

    .panel-code{

        width: 30%;
        height: 25%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 99999;
        background: #fff;
        border-radius: 15px;
        padding: 15px;

        h1{

            margin: 20px 0;

        }

        p{

            margin: 20px 0;

        }

        input{

            @include inputs();
            margin: 20px 0;
            text-align: center;

        }

    }

</style>