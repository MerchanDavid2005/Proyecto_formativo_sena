<template>
    
    <div class="todo">

        <NavTop @panel="abrirCerrarPanel" />

        <div class="todo-contenido">

            <div class="todo-contenido-panel">

                <transition name="panel">
                    <PanelOptionsVue v-show="panel" @nuevo="mostrarTabla" />
                </transition>

            </div>
        
            <div 
            
                :class="{
                    'todo-contenido-info-ok': panel == false,
                    'todo-contenido-info-none': panel == true || tablaMostrada == true || pinia.cargandoDatos,
                    'todo-contenido-info-dark': pinia.temaClaro == false
                }">

                <slot></slot>

            </div>

            <div :class="{'todo-contenido-new': pinia.temaClaro, 'todo-contenido-new-dark': pinia.temaClaro == false}">
                
                <component v-show="tablaMostrada" :is="tablaCreacion" @cerrar="ocultarTabla" />

            </div>

            <div class="todo-contenido-load">

                <LoaderCompVue v-show="pinia.cargandoDatos" />

            </div>

            <div class="todo-contenido-mensaje">

                <transition name="mensaje">
                
                    <MessagesSuccess v-show="pinia.exitoFetch" />

                </transition>

                <transition name="mensaje">
                
                    <MessagesError v-show="pinia.errorFetch" />

                </transition>

            </div>

        </div>

    </div>

</template>

<script setup>

    import NavTop from '@/components/NavTop.vue';
    import PanelOptionsVue from '../components/PanelOptions.vue';
    import LoaderCompVue from '../components/LoaderComp.vue';
    import MessagesSuccess from '@/components/MessagesSuccess.vue';
    import MessagesError from '@/components/MessagesError.vue';

    import { ref, defineAsyncComponent } from 'vue'
    import { useStore } from '@/store/pinia';

    const pinia = useStore()

    let panel = ref(false)
    let tablaCreacion = ref()
    let tablaMostrada = ref(false)

    let tablaProducto = defineAsyncComponent(() => import('@/components/NewProduct.vue'))
    let tablaCategoria = defineAsyncComponent(() => import('@/components/NewCategory.vue'))
    let tablaServicio = defineAsyncComponent(() => import('@/components/NewService.vue'))

    const abrirCerrarPanel = () => {

        if(panel.value){

            panel.value = false
            pinia.colorLetraPanel = 'transparent'

        }else{

            panel.value = true
            pinia.colorLetraPanel = '#fff'

        }

    }

    function mostrarTabla(tabla){

        abrirCerrarPanel()

        if(tabla == 'producto'){

            tablaCreacion = tablaProducto
            tablaMostrada.value = true

        }else if(tabla == 'categoria'){

            tablaCreacion = tablaCategoria
            tablaMostrada.value = true

        }else{

            tablaCreacion = tablaServicio
            tablaMostrada.value = true

        }

    }

    const ocultarTabla = () => tablaMostrada.value = false

</script>

<style lang="scss" scoped>

    .todo{

        width: 100%;
        height: 100vh;

        &-contenido{

            height: 90vh;
            width: 100%;
            display: flex;

            &-panel{

                width: 100%;
                height: 90vh;
                display: flex;
                justify-content: flex-start;
                position: absolute;

            }

            &-info-ok{

                width: 100%;
                height: 100%;
                display: flex;
                background: #fff;
                filter: brightness(100%);
                pointer-events: all;
                transition: all 0.5s ease-in-out;
                position: static;
                z-index: 10;

            }

            &-info-none{

                width: 100%;
                height: 100%;
                display: flex;
                background: #444;
                filter: brightness(20%);
                pointer-events: none;
                transition: all 0.5s ease-in-out;
                position: static;
                z-index: 10;

            }

            &-info-dark{

                width: 100%;
                height: 100%;
                display: flex;
                background: #000;
                color: #fff;
                position: static;
                z-index: 10;

            }

            &-new{

                width: 100%;
                height: 90vh;
                display: flex;
                justify-content: center;
                align-items: center;
                position: absolute;
                color: #000;

            }

            &-new-dark{

                width: 100%;
                height: 90vh;
                display: flex;
                justify-content: center;
                align-items: center;
                position: absolute;
                color: #fff;

            }

            &-load{

                width: 100%;
                height: 90vh;
                display: flex;
                position: absolute;

            }

            &-mensaje{

                width: 100%;
                height: 90vh;
                display: flex;
                justify-content: flex-end;
                align-items: flex-start;
                position: absolute;
                box-sizing: border-box;
                padding: 2%;
                overflow: hidden;

            }

        }

    }

    @keyframes mensaje {
        
        0%{

            transform: translateX(500px);

        }
        50%{

            transform: translateX(-50px);

        }
        100%{

            transform: translateX(0);

        }

    }

    .panel-enter-active, .panel-leave-active{

        transition: height 0.5s ease;

    }

    .panel-enter-from, .panel-leave-to{

        height: 0%;

    }

    .mensaje-enter-active{

        animation: mensaje 1s ease;

    }

    .mensaje-leave-active{

        animation: mensaje 1s ease reverse;
    
    }

</style>