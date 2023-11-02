<template>

    <div class="error-load-view">
        
        <ErrorComp />
        <AnimationErrorPage />
        
    </div>

</template>

<script lang="ts" setup>

    import ErrorComp from '../components/ErrorComp.vue';
    import AnimationErrorPage from '../components/AnimationErrorPage.vue';

    import { useRouter } from 'vue-router';

    const enrutado = useRouter()

    if(sessionStorage.getItem("error") == "false"){

        enrutado.push('/')

    }

</script>

<style lang="scss" scoped>

    .error-load-view{

        width: 100%;
        height: 100vh;
        background: #000;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

    }

</style>
