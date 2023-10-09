<template>
    
    <div class="todo">

        <NavTop @panel="abrirCerrarPanel" />

        <div class="todo-contenido">

            <div class="todo-contenido-panel">

                <transition name="panel">
                    <PanelOptionsVue v-show="panel" />
                </transition>

            </div>
        
            <div 
            
                :class="{
                    'todo-contenido-info-ok': panel == false,
                    'todo-contenido-info-none': panel == true,
                    'todo-contenido-info-dark': pinia.temaClaro == false
                }">

                <slot></slot>

            </div>

        </div>

    </div>

</template>

<script setup>

    import NavTop from '@/components/NavTop.vue';
    import PanelOptionsVue from '../components/PanelOptions.vue';

    import { ref } from 'vue'
    import { useStore } from '@/store/pinia';

    let panel = ref(false)
    const pinia = useStore()

    const abrirCerrarPanel = () => {

        if(panel.value){

            panel.value = false
            pinia.colorLetraPanel = 'transparent'

        }else{

            panel.value = true
            pinia.colorLetraPanel = '#fff'

        }

    }

</script>

<style lang="scss" scoped>

    .todo{

        width: 100%;
        height: 100vh;

        &-contenido{

            height: 90vh;
            width: 100%;

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

            }

            &-info-none{

                width: 100%;
                height: 100%;
                display: flex;
                background: #444;
                filter: brightness(20%);
                pointer-events: none;
                transition: all 0.5s ease-in-out;

            }

            &-info-dark{

                width: 100%;
                height: 100%;
                display: flex;
                background: #000;
                color: #fff;

            }

        }

    }

    .panel-enter-active, .panel-leave-active{

        transition: height 0.5s ease;

    }

    .panel-enter-from, .panel-leave-to{

        height: 0%;

    }

</style>