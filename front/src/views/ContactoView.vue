<template>
    <MainDefault>

        <div class="contact-view">

            <ContactCompVue />

        </div>

    </MainDefault>
</template>

<script lang="ts" setup>

    import ContactCompVue from '../components/ContactComp.vue';
    import MainDefault from '../layouts/MainDefault.vue';

</script>

<style lang="scss" scoped>

    .contact-view{

        width: 100%;
        height: 90vh;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: auto;

    }

</style>