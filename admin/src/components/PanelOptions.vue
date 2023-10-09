<template>

    <div class="panel" :style="{background: pinia.fondoFiltros, color: pinia.colorLetraPanel}">

        <div class="panel-data">
            <div class="panel-data-avatar">
                <img src="https://pbs.twimg.com/profile_images/1390430745705975811/PTN2XO5S_400x400.jpg" alt="">
            </div>
            <h1 
                :class="{'panel-data-titulo': pinia.letraPanel, 'panel-data-titulo-dark': pinia.letraPanel == false}"> 
                LAMWL 
            </h1>
        </div>
        <div class="panel-crear">
            <div class="panel-crear-producto"> 
                <p> Nuevo producto  </p>
                <v-icon name="md-fibernew-round" scale="1.5"></v-icon>
            </div>
            <div class="panel-crear-categoria"> 
                <p> Nueva categoria  </p>
                <v-icon name="io-duplicate" scale="1.5"></v-icon>
            </div>
            <div class="panel-crear-servicio"> 
                <p> Nuevo servicio  </p>
                <v-icon name="md-task" scale="1.5"></v-icon>
            </div>
        </div>
        <div class="panel-ajustes">
            <div class="panel-ajustes-tema">
                <v-icon name="md-lightmode" scale="1.5"></v-icon>
                <div class="panel-ajustes-tema-barra">
                    <div 
                        @click="cambioTema" 
                        :class="{'panel-ajustes-tema-barra-boton-light': pinia.temaClaro, 'panel-ajustes-tema-barra-boton-dark': !pinia.temaClaro}">
                    </div>
                </div>
                <v-icon name="md-darkmode" scale="1.5"></v-icon>
            </div>
            <div class="panel-ajustes-sesion">
                <p> Cerrar sesion </p>
                <v-icon name="md-powersettingsnew-sharp" scale="1.5"></v-icon>
            </div>
        </div>

    </div>

</template>

<script setup>

    import { useStore } from '@/store/pinia'

    const pinia = useStore()

    function cambioTema(){

        if(pinia.temaClaro){

            pinia.temaClaro = false
            pinia.fondoFiltros = '#004'
            pinia.greentheme = '#084'
            pinia.fondoEdits = '#444'

        }else{

            pinia.temaClaro = true
            pinia.fondoFiltros = '#0af'
            pinia.greentheme = '#0fa'
            pinia.fondoEdits = '#fff'

        }

    }

</script>

<style lang="scss" scoped>

    .panel{

        width: 15%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        position: absolute;
        z-index: 999999;
        color: #fff;
        border-right: 2px solid #fff;
        transition: background 0.5s ease;

        &-data{

            width: 100%;
            height: 40%;
            display: flex;
            flex-direction: column;
            align-items: center;
    
            &-avatar{
    
                width: 60%;
                height: 70%;
                clip-path: circle(50%);
    
            }

            &-titulo{

                width: 100%;
                height: 20%;
                display: flex;
                justify-content: center;
                align-items: center;
    
            }

        }

        &-crear{

            width: 80%;
            height: 40%;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            justify-content: space-evenly;
            border-top: 2px solid #fff;
            border-bottom: 2px solid #fff;

            div{

                width: 100%;
                display: flex;
                justify-content: space-evenly;

                p{

                    font-size: 20px;
                    cursor: pointer;

                }

            }

            div:hover{

                color: #444;

            }

        }

        &-ajustes{

            width: 100%;
            height: 20%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-evenly;

            &-tema{

                width: 100%;
                height: 40%;
                display: flex;
                align-items: center;
                justify-content: space-evenly;

                &-barra{

                    width: 20%;
                    height: 20%;
                    background: $forth-color;
                    border-radius: 20px;
                    display: flex;
                    align-items: center;
                    justify-content: flex-start;

                    &-boton-light{

                        width: 60%;
                        height: 250%;
                        background: #ddd;
                        border-radius: 100%;
                        cursor: pointer;
                        transform: translateX(-20%);
                        transition: transform 0.5s cubic-bezier(1, 1, 1, 1);

                    }

                    &-boton-dark{

                        width: 60%;
                        height: 250%;
                        background: #ddd;
                        border-radius: 100%;
                        cursor: pointer;
                        transform: translateX(100%);
                        transition: transform 0.5s cubic-bezier(1, 1, 1, 1);

                    }

                }

            }

            &-sesion{

                width: 100%;
                height: 40%;
                display: flex;
                flex-direction: column-reverse;
                align-items: center;
                justify-content: center;

                p{

                    margin: 0 10px;

                }

            }

        }

    }

</style>