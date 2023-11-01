<template>

    <div class="todo">

        <div class="todo-cabeza">

            <NavBar />

        </div>

        <div class="todo-contenido">

            <slot></slot>

        </div>

        <div class="todo-carga">

            <LoaderComp v-show="pinia.pantallaCarga" />

        </div>

    </div>

</template>

<script lang="ts" setup>

    import NavBar from '../components/NavBar.vue';
    import LoaderComp from '../components/LoaderComp.vue';

    import { useStore } from '../store/pinia'

    const pinia = useStore()

</script>

<style lang="scss" scoped>

    .todo{

        width: 100%;
        height: 100vh;
        display: flex;
        flex-direction: column;

        &-cabeza{

            width: 100%;
            height: 10%;
            position: static;
            z-index: 10;

        }

        &-contenido{

            width: 100%;
            height: 90%;
            position: static;
            z-index: 10;

        }

        &-carga{

            width: 100%;
            height: 90%;
            display: flex;
            position: absolute;

        }

    }

</style>