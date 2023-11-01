<template>

    <div class="cuerpo-login">
        
        <h1 class="cuerpo-login-titulo"> Registrarse </h1>

        <p v-if="errorCampos" class="error"> Por favor no dejes ningun campo vacio </p>
        <p v-if="errorContraseñas" class="error"> Las contraseñas no coinciden </p>

        <div class="cuerpo-login-body">

            <div class="cuerpo-login-body-info">

                <div class="cuerpo-login-body-info-fila">
    
                    <div class="cuerpo-login-body-info-fila-columna">
    
                        <p> Nombre de usuario </p>
                        <input v-model="usuario" type="text" placeholder="Usuario">
    
                    </div>
    
                    <div class="cuerpo-login-body-info-fila-columna">
    
                        <p> Nombre </p>
                        <input v-model="nombre" type="text" placeholder="Nombre">
    
                    </div>
    
                </div>
    
                <div class="cuerpo-login-body-info-fila">
    
                    <div class="cuerpo-login-body-info-fila-columna">
    
                        <p> Correo </p>
                        <input v-model="correo" type="text" placeholder="Correo">
    
                    </div>
                    
                    <div class="cuerpo-login-body-info-fila-columna">
              
                        <p> Foto de perfil ( opcional ) </p>
                        <input type="file" :onchange="valorImagen">
    
                    </div>
    
                </div>
    
                <div class="cuerpo-login-body-info-fila">
    
                    <div class="cuerpo-login-body-info-fila-columna">
    
                        <p> Contraseña </p>
                        <input v-model="contraseña" type="password" placeholder="Contraseña">
    
                    </div>
    
                    <div class="cuerpo-login-body-info-fila-columna">
    
                        <p> Verifica tu contraseña </p>
                        <input v-model="contraseñaVerificacion" type="password" placeholder="Verificar contraseña">
    
                    </div>
    
                </div>
    
                <div class="cuerpo-login-body-info-mensajes">
    
                    <p> ¿Ya tienes una cuenta?  </p>
                    <p> Inicia sesion siguiendo el siguien enlace 
                        <router-link to="/"> iniciar sesion </router-link>
                    </p>
                    <button @click="cargarDatos"> Registrarse </button>
    
                </div>
    
            </div>
    
            <div class="cuerpo-login-body-imagen">
    
                <img :src="imagenMostrar" alt="foto-perfil">
    
            </div>

        </div>

    </div>

</template>

<script setup>

    import { ref, defineEmits } from 'vue';
    import { useStore } from '@/store/pinia'

    const emits = defineEmits(['mostrarCodigo'])
    const pinia = useStore()

    let usuario = ref("")
    let nombre = ref("")
    let correo = ref("")
    let imagen = ref()
    let contraseña = ref("")
    let contraseñaVerificacion = ref("")

    let errorContraseñas = ref(false)
    let errorCampos = ref(false)

    let imagenMostrar = ref("https://laadministracionelectronica.files.wordpress.com/2014/10/fondo1.jpg") 

    const valorImagen = (img) => {
        
        imagenMostrar.value = URL.createObjectURL(img.target.files[0])
        imagen.value = img.target.files[0]

    }

    function validar(){

        let validado = false

        if(usuario.value.trim().length > 0 && nombre.value.trim().length > 0 && correo.value.trim().length > 0 && contraseña.value.trim().length > 0){

            if(contraseña.value == contraseñaVerificacion.value){

                validado = true

            }
            else{

                validado = false
                errorContraseñas.value = true

            }
        
        }else{

            validado = false
            errorCampos.value = true

        }

        return validado

    }

    const panelVerificacion = async () => {

        if(validar()){

            emits('mostrarCodigo')

            pinia.datosUsuarioCrear.push(usuario.value)
            pinia.datosUsuarioCrear.push(nombre.value)
            pinia.datosUsuarioCrear.push(correo.value)
            pinia.datosUsuarioCrear.push(imagen.value)
            pinia.datosUsuarioCrear.push(contraseña.value)

            const peticion = await fetch("http://localhost:8000/send/code/verify/", {

                method: 'POST',
                body: JSON.stringify({

                    usuario: usuario.value,
                    email: correo.value

                }),
                headers: {"content-type": "application/json"}

            })

            return peticion.json()

        }else{

            return {"Codigo": "Error"}

        }

    }

    const cargarDatos = async () => {

        try{

            const codigo = await panelVerificacion()

            if(codigo.Codigo !== "Error") pinia.codigoVerificacion = codigo.Codigo

        }
        catch(e){

            pinia.errorFetch = true
            setTimeout(() => {

                pinia.errorFetch = false

            }, 3000)

        }

    }

</script>

<style lang="scss" scoped>

    .cuerpo-login{

        height: 80%;
        width: 65%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 15px;
        border-radius: 15px;
        position: static;
        z-index: 100;
        background: #fff;

        &-titulo{

            width: 100%;
            text-align: center;
            height: 15%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 50px;

        }

        .error{

            text-align: center;
            color: #f00;

        }

        &-body{

            width: 100%;
            height: 80%;
            display: flex;
            justify-content: space-around;
            align-items: center;
            
            &-info{

                width: 45%;
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: space-evenly;

                &-fila{

                    width: 100%;
                    display: flex;
                    justify-content: space-evenly;

                    &-columna{

                        display: flex;
                        flex-direction: column;
                        width: 45%;

                        input{

                            @include inputs();
                            margin: 10px 0;

                        }

                    }

                }

                &-mensajes{

                    width: 100%;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    font-size: 15px;

                    p{

                        margin: 5px 0;

                    }

                    button{

                        @include botones();
                        background: $second-color;
                        margin: 10px 0;

                    }

                }

            }

            &-imagen{

                width: 45%;
                height: 100%;
                padding: 10px;

            }

        }

    }

</style>