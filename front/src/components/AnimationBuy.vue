<template>
    <div class="cuerpo-animacion">

        <transition name="salir">
            <h1 :style="{opacity: opacidad}" @click="emits('ocultar')"> Aceptar </h1>
        </transition>
        
        <div class="cuerpo-animacion-espacio">

            <v-icon 
                :class="{'animationNone' : animacionStart == false, 'animationStart' : animacionStart}" 
                :name="icono" 
                scale="10">
            </v-icon>

        </div>

    </div>
</template>

<script lang="ts" setup>

    import { ref, defineEmits } from "vue";

    const emits = defineEmits(['ocultar'])

    let icono = ref<string>("bi-cart-fill")
    let opacidad = ref<string>("0")
    let animacionStart = ref<boolean>(false)

    setTimeout(() => {

        animacionStart.value = true

    }, 1000)

    setTimeout(() => {

        icono.value = ("bi-cart-check-fill")

    }, 3500)

    setTimeout(() => {

        opacidad.value = "1"

    }, 5000)

</script>

<style lang="scss" scoped>

    .cuerpo-animacion{

        width: 100%;
        height: 100%;
        background: #222;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: absolute;
        z-index: 100000;

        &-espacio{

            width: 100%;
            height: 30%;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            background: #ddd;
            margin: 50px 0;

            .animationNone{

                animation-duration: 5s;
                animation-fill-mode: forwards;
                animation-timing-function: cubic-bezier(0.45, 1, 0.165, 1);
                color: #000;
    
            }

            .animationStart{

                animation-name: comprado;
                animation-duration: 4s;
                animation-fill-mode: forwards;
                animation-timing-function: cubic-bezier(0.75, 1, 0.165, 1);
                color: #000;
    
            }

        }

        h1{

            color: $fondo-boton-crear;
            font-size: 40px;
            cursor: pointer;
            transition: opacity 0.5s ease;

        }

    }

    @keyframes comprado {

        0%{

            transform: translateX(0) rotateZ(-10deg);

        }

        40%{

            transform: translateX(1500px) rotateZ(-10deg);

        }

        60%{

            transform: translateY(-1500px);

        }

        100%{

            transform: rotateY(0deg);
            color: $fondo-boton-crear;

        }
        
    }

</style>