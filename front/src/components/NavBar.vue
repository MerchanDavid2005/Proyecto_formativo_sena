<template>
    <nav class="nav">
        <div class="nav-title">
            <h1> Serviteca la estacion </h1>
        </div>
        <div class="nav-urls">
            <ul>
                <router-link style="text-decoration: none;" :to="{name: 'productos', params: {id: 1}}">
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
                <router-link style="text-decoration: none;" :to="{name: 'datos'}">
                    <li> 
                        <v-icon name="fa-database" scale="1.6"></v-icon>
                        Datos 
                    </li>
                </router-link>
            </ul>
        </div>
        <div class="nav-tema">
            <v-icon name="md-lightmode" scale="1.6"></v-icon>
            <div class="nav-tema-divButton">
                <button 
                    @click="pinia.claro = !pinia.claro"
                    :class="{'boton-claro' : pinia.claro, 'boton-oscuro' : !pinia.claro}">
                </button>
            </div>
            <v-icon name="md-darkmode" scale="1.6"></v-icon>
        </div>
    </nav>
</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia'

    const pinia = useStore()

</script>

<style lang="scss" scoped>

    .nav{

        width: 100%;
        height: 10vh;
        background: #0af;
        display: flex;
        align-items: center;
        justify-content: space-evenly;

        &-title{

            height: 50%;
            width: 35%;
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
            width: 50%;
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

        &-tema{

            width: 10%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: space-evenly;
            color: #fff;

            &-divButton{

                width: 30%;
                height: 20%;
                background: $fondo-input;
                border-radius: 20px;
                display: flex;
                align-items: center;

                .boton-claro{

                    width: 65%;
                    height: 200%;
                    border-radius: 100%;
                    border: 0;
                    background: #fff;
                    transform: translateX(0px);
                    transition: transform 0.5s ease;

                }

                .boton-oscuro{

                    width: 65%;
                    height: 200%;
                    border-radius: 100%;
                    border: 0;
                    background: #fff;
                    transform: translateX(15px);
                    transition: transform 0.5s ease;

                }

            }

        }

    }

</style>