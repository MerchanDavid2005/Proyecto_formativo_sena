<template>

    <div class="error-load">
        
        <ErrorComp />
        
    </div>

</template>

<script lang="ts" setup>

    import ErrorComp from '../components/ErrorComp.vue';

</script>

<style lang="scss" scoped>

    .error-load{

        width: 100%;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;

    }

</style>
