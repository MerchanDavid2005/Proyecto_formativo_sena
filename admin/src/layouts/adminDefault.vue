<template>

    <div class="todo">

        <NavTop />

        <div class="todo-contenido">

            <slot></slot>

        </div>

    </div>

</template>

<script setup>

    import NavTop from '@/components/NavTop.vue'

</script>

<style lang="scss" scoped>

    .todo{

        width: 100%;
        height: 100vh;

        &-contenido{

            display: flex;
            justify-content: flex-start;
            height: 90vh;
            width: 100%;

        }

    }

</style>