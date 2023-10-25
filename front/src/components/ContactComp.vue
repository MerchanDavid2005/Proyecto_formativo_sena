<template>

    <div class="contact-comp">

        <div class="contact-comp-title">
            <h1> ¡Bienvenido! </h1>
            <p class="error" v-show="error"> Por favor no dejes campos en blanco </p>
            <p> En este apartado podras contactar conmigo ya sea por errores de nuestra pagina o si deseas contactar conmigo por diferentes razones </p>
        </div>
        <div class="contact-comp-body">
            <div class="contact-comp-body-info">
                <div class="contact-comp-body-info-campo-doble">
                    <div class="contact-comp-body-info-campo-doble-name">
                        <label> Nombre: </label>
                        <input v-model="nombre" type="text" placeholder="Nombre">
                    </div>
                    <div class="contact-comp-body-info-campo-doble-razon">
                        <label> Motivo: </label>
                        <select>
                            <option v-for="i in motivosCorreo" :key="i" :value="i"> {{ i }} </option>
                        </select>
                    </div>
                </div>
                <div class="contact-comp-body-info-campo">
                    <label> Texto descriptivo:  </label>
                    <textarea v-model="descripcion" rows="5"></textarea>
                </div>
                <div class="contact-comp-body-info-campo">
                    <label> Imagen descriptiva: ( opcional ) </label>
                    <input type="file" :onchange="valorImagen">
                </div>
                <div class="contact-comp-body-info-button">
                    <button @click="enviarCorreo"> Enviar </button>
                </div>
            </div>
            <div class="contact-comp-body-imagen">
                <img :src="imagenDemostracion" alt="">
            </div>
        </div>
        <div class="contact-comp-end">
            <p> No es necesario ingresar un correo, nuestro sistema esta diseñado para usar un correo anonimo con el cual puedas contactarte </p>
        </div>
        
    </div>

</template>

<script lang="ts" setup>

    import { ref } from 'vue'
    import { useRouter } from 'vue-router';
    import { useStore } from '../store/pinia';

    const pinia = useStore()
    const enrutado = useRouter()

    let nombre = ref<string>("")
    let motivo = ref<string>("Error")
    let descripcion = ref<string>("Descripcion del problema o necesidad")
    let imagen = ref<string>("")
    let imagenDemostracion = ref<string>("https://www.lavanguardia.com/andro4all/hero/2021/01/aplicaciones-aprender-mecanica.jpg?width=768&aspect_ratio=16:9&format=nowebp")

    let error = ref<boolean>(false)

    let motivosCorreo = ref<Array<string>>([

        "Error",
        "Ayuda",
        "Contactarme",
        "Otro"

    ])

    const valorImagen = (img: any) => {
        
        imagen.value = img.target.files[0]

        try{
            imagenDemostracion.value = URL.createObjectURL(img.target.files[0])
        }catch(e){
            console.log(e)
        }

    }

    async function guardarImagen(){

        if(imagen.value != ""){

            let cuerpoInfo = new FormData()

            cuerpoInfo.append("imagen", imagen.value)

            const data = await fetch("http://localhost:8000/save/img/correo/", {

                method: 'POST',
                body: cuerpoInfo

            })

            return data.json()

        }else{

            return "No hay imagen"

        }

    }

    async function enviarCorreo(){

        await guardarImagen();

        if(nombre.value != "" && descripcion.value != ""){

            let infoCorreo = new FormData()

            infoCorreo.append("nombre", nombre.value)
            infoCorreo.append("motivo", motivo.value)
            infoCorreo.append("descripcion", descripcion.value)
            infoCorreo.append("imagen", imagen.value)

            fetch("http://localhost:8000/send/email/contact/", {

                method: 'POST',
                body: infoCorreo

            })

            enrutado.push("/")

            setTimeout(() => {

                pinia.correoContactoEnviado = true

            }, 500)

            setTimeout(() => {

                pinia.correoContactoEnviado = false

            }, 4000)

        }else{

            error.value = true

        }

    }

</script>

<style lang="scss" scoped>

    .contact-comp{

        width: 70%;
        height: 85%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        background: $fondo-input;
        border-radius: 15px;
        padding: 25px;
        color: #000;

        &-title{

            width: 100%;
            height: 15%;
            display: flex;
            flex-direction: column;
            align-items: center;

            h1{

                margin-bottom: 10px;

            }

        }

        .error{

            text-align: center;
            color: #f00;
            margin: 5px 0;

        }

        &-body{

            width: 100%;
            height: 75%;
            display: flex;
            align-items: center;
            justify-content: space-evenly;

            &-info{

                width: 45%;
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: space-evenly;

                &-campo-doble{

                    width: 100%;
                    height: max-content;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;

                    &-name{

                        width: 45%;
                        height: max-content;
                        display: flex;
                        flex-direction: column;

                        input{

                            @include inputs();
                            background: #fff;

                        }

                    }

                    &-razon{

                        width: 45%;
                        height: max-content;
                        display: flex;
                        flex-direction: column;

                        select{

                            @include inputs();
                            background: #fff;

                        }

                    }

                }

                &-campo{

                    width: 100%;
                    height: max-content;
                    display: flex;
                    flex-direction: column;

                    input{

                        @include inputs();
                        background: #fff

                    }

                    textarea{

                        @include inputs();   
                        background: #fff;    
                        height: max-content; 

                    }

                    input[type="file"]{

                        color: #000;
                        background: #fff

                    }
                        
                }

                &-button{

                    width: 100%;
                    height: max-content;
                    display: flex;

                    button{

                        @include botones($fondo-boton-limpiar);
                        color: #fff;
                        font-weight: 100;
                        width: 50%;

                    }

                }
                
            }
    
            &-imagen{
    
                width: 45%;
                height: 100%;
                display: flex;
                align-items: center;
                justify-content: center;
    
            }

        }

        &-end{

            width: 100%;
            height: 5%;
            text-align: center;

        }

    }

</style>