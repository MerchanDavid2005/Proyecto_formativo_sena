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

            let bodyData = new FormData

            bodyData.append("usuario", pinia.datosUsuarioCrear[0]);
            bodyData.append("nombre", pinia.datosUsuarioCrear[1]);
            bodyData.append("email", pinia.datosUsuarioCrear[2]);
            bodyData.append("img", pinia.datosUsuarioCrear[3]);
            bodyData.append("password", pinia.datosUsuarioCrear[4]);

            fetch("http://localhost:8000/post/user/", {

                method: 'POST',
                body: bodyData

            });

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
        height: 35%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 99999;
        background: #fff;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0 15px 15px 0 #555;

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