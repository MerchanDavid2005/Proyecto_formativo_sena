<template>
    <nav class="nav">
        <div class="nav-title">
            <h1> Serviteca la estacion </h1>
        </div>
        <div class="nav-urls">
            <ul>
                <router-link style="text-decoration: none;" :to="{name: 'productos'}">
                    <li> 
                        <v-icon name="md-home-round" scale="1.6"></v-icon>
                        Inicio 
                    </li>
                </router-link>
                <router-link style="text-decoration: none;" :to="{name: 'carrito'}">
                    <li> 
                        <v-icon name="bi-cart-fill" scale="1.6"></v-icon>
                        Carrito 
                    </li>
                </router-link>
                <router-link style="text-decoration: none;" :to="{name: 'servicios'}">
                    <li> 
                        <v-icon name="md-work-sharp" scale="1.6"></v-icon>
                        Servicios 
                    </li>
                </router-link>
                <router-link style="text-decoration: none;" :to="{name: 'contacto'}">
                    <li> 
                        <v-icon name="md-contactmail" scale="1.6"></v-icon>
                        Contacto 
                    </li>
                </router-link>
            </ul>
        </div>
        <div class="nav-account">
            <div @click="abrirPanel" class="nav-account-img">
                <img :src="pinia.datosUsuario.foto" alt="">
            </div>
            <div @click="iniciarSesion" v-show="panel && !pinia.usuarioLogeado" class="nav-account-panel">
                <v-icon name="hi-login" scale="2"></v-icon>
                <h1> Iniciar sesion </h1>
            </div>
            <div @click="enrutado.push('/perfil')" v-show="panel && pinia.usuarioLogeado" class="nav-account-panel">
                <v-icon name="md-accountcircle" scale="2"></v-icon>
                <h1> Mi cuenta </h1>
            </div>
        </div>
    </nav>
</template>

<script lang="ts" setup>

    import { ref } from 'vue'
    import { useRouter } from 'vue-router';
    import { useStore } from '../store/pinia'

    const pinia = useStore()
    const enrutado = useRouter()

    let panel = ref(false)

    const abrirPanel = () => panel.value = !panel.value

    const iniciarSesion = () => enrutado.push('/iniciar_sesion')

</script>

<style lang="scss" scoped>

    .nav{

        width: 100%;
        height: 100%;
        background: #0af;
        display: flex;
        align-items: center;
        justify-content: space-evenly;

        &-title{

            height: 50%;
            width: 30%;
            border-right: 5px solid #fff;
            display: flex;
            justify-content: center;
            align-items: center;

            h1{

                color: #fff;
                font-weight: bold;
                font-size: 30px;

            }

        }

        &-urls{

            height: 60%;
            width: 55%;
            border-right: 5px solid #fff;

            ul{

                width: 100%;
                height: 100%;
                display: flex;
                justify-content: space-evenly;
                align-items: center;
                list-style: none;

                li{

                    color: #fff;
                    font-weight: bold;
                    font-size: 15px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;

                }

                li:hover{

                    color: #bbb;

                }

            }

        }

        &-account{

            width: 10%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;

            &-img{

                width: max-content;
                height: 70%;
                cursor: pointer;
                clip-path: circle(50%);

            }

            &-panel{

                width: 10%;
                position: fixed;
                z-index: 1000;
                top: 10vh;
                height: max-content;
                background: $fondo-boton-limpiar;
                display: flex;
                flex-direction: column;
                align-items: center;
                box-sizing: border-box;
                padding: 1%;
                border-radius: 0 0 10px 10px;
                color: #fff;
                cursor: pointer;

                h1{

                    font-size: 18px;
                    margin-top: 10px;
                    text-align: center;

                }

            }

            &-panel:hover{

                background: #09f;

            }

        }
    }

</style>