<template>
    <MainDefault>

        <div class="cuerpo-perfil">

            <div :class="{'cuerpo-perfil-contenido': !panel && !panelDeleteAccount, 'cuerpo-perfil-contenido-none': panel || panelDeleteAccount}">

                <AccountComp @verify="abrirPanel" />
                <OrdersAll />
    
            </div>
    
            <div class="cuerpo-perfil-verify">
    
                <component :is="cuadro" v-show="panel" @verify="abrirPanel" @verifyDelete="panelEliminarcuenta"></component>
                <VerifyDeleteAccount v-show="panelDeleteAccount" @verifyDelete="panelEliminarcuenta" />
    
            </div>

        </div>

    </MainDefault>
</template>

<script lang="ts" setup>

    import MainDefault from '../layouts/MainDefault.vue';
    import OrdersAll from '../components/OrdersAll.vue';
    import AccountComp from '../components/AccountComp.vue';
    import VerifyDeleteAccount from '../components/VerifyDeleteAccount.vue'

    import { ref, defineAsyncComponent, shallowRef } from 'vue'

    let panel = ref<boolean>(false)
    let panelDeleteAccount = ref<boolean>(false)

    let cuadroEditar = defineAsyncComponent(() => import('../components/VerifyDelete.vue'))

    let cuadro = shallowRef(cuadroEditar)

    const abrirPanel = (tabla: any) => {
        
        panel.value = !panel.value
        cuadro.value = tabla

    }

    const panelEliminarcuenta = () => {
        
        panelDeleteAccount.value = !panelDeleteAccount.value
        panel.value = false

    }

</script>

<style lang="scss" scoped>

    .cuerpo-perfil{

        width: 100%;
        height: 90vh;
        display: flex;

        &-contenido{

            width: 100%;
            height: 90vh;
            padding-top: 5vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            box-sizing: border-box;
            overflow: auto;
            position: static;
            z-index: 10;
            transition: all 0.5s ease-in-out;

        }

        &-contenido-none{

            width: 100%;
            height: 90vh;
            padding-top: 5vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            box-sizing: border-box;
            overflow: auto;
            position: static;
            z-index: 10;
            filter: brightness(20%);
            background: #444;
            transition: all 0.5s ease-in-out;

        }

        &-verify{

            width: 100%;
            height: 90vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: auto;
            position: absolute;

        }

    }

</style>