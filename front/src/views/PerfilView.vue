<template>
    <MainDefault>

        <div class="cuerpo-perfil">

            <div class="cuerpo-perfil-contenido">

                <AccountComp @verify="abrirPanel" />
                <OrdersAll />
    
            </div>
    
            <div class="cuerpo-perfil-verify">
    
                <VerifyEdit v-show="panel" @verify="abrirPanel" />
    
            </div>

        </div>

    </MainDefault>
</template>

<script lang="ts" setup>

    import MainDefault from '../layouts/MainDefault.vue';
    import OrdersAll from '../components/OrdersAll.vue';
    import AccountComp from '../components/AccountComp.vue';
    import VerifyEdit from '../components/VerifyEdit.vue';

    import { ref } from 'vue'

    let panel = ref<boolean>(false)

    const abrirPanel = () => panel.value = !panel.value

</script>

<style lang="scss" scoped>

    .cuerpo-perfil{

        width: 100%;
        height: 90vh;
        display: flex;

        &-contenido{

            width: 100%;
            height: 85vh;
            padding-top: 5vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            box-sizing: border-box;
            overflow: auto;
            position: static;
            z-index: 100;

        }

        &-verify{

            width: 100%;
            height: 85vh;
            display: flex;
            align-items: center;
            overflow: auto;
            position: absolute;
            z-index: 1;

        }

    }

</style>