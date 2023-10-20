<template>

    <div class="panel-code">
        
        <h1> Codigo de verificacion </h1>
        <p> Se ha enviado un codigo de verificacion al email introducido, por favor ingresa el codigo enviado </p>
        <input v-model="code" type="text" placeholder="XXXXXX" maxlength="6">

    </div>

</template>

<script lang="ts" setup>

    import { ref, watch } from 'vue'
    import { useStore } from '@/store/pinia';
    import { useRouter } from 'vue-router';

    const enrutado = useRouter()
    const pinia = useStore()

    let code = ref("")

    watch(code, () => {

        if(code.value == pinia.codigoVerificacion){

            let bodyData = new FormData

            bodyData.append("usuario", pinia.datosUsuarioCrear.usuario);
            bodyData.append("nombre", pinia.datosUsuarioCrear.nombre);
            bodyData.append("email", pinia.datosUsuarioCrear.correo);
            bodyData.append("img", pinia.datosUsuarioCrear.img);
            bodyData.append("password", pinia.datosUsuarioCrear.password);

            fetch("http://localhost:8000/post/user/Client/", {

                method: 'POST',
                body: bodyData

            });

            enrutado.push('/iniciar_sesion')

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
        position: absolute;
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