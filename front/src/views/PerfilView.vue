<template>
    <MainDefault>

        <div class="cuerpo-perfil">

            <div :class="{'cuerpo-perfil-contenido': !panel, 'cuerpo-perfil-contenido-none': panel}">

                <AccountComp @verify="abrirPanel" />
                <OrdersAll />
    
            </div>
    
            <div class="cuerpo-perfil-verify">
    
                <PanelDeleteAccount v-show="panelEliminar" @verify="abrirPanel" @ocultar="ocultarTodo" />
                <VerifyEdit v-show="panelEditar" @ocultar="ocultarTodo" />
                <VerifyDeleteAccount v-show="panelEliminarConfirmar" @ocultar="ocultarTodo" />
    
            </div>

        </div>

    </MainDefault>
</template>

<script lang="ts" setup>

    import MainDefault from '../layouts/MainDefault.vue';
    import OrdersAll from '../components/OrdersAll.vue';
    import AccountComp from '../components/AccountComp.vue';
    import PanelDeleteAccount from '../components/PanelDeleteAccount.vue';
    import VerifyEdit from '../components/VerifyEdit.vue'
    import VerifyDeleteAccount from '../components/VerifyDeleteAccount.vue';

    import { ref } from 'vue'

    let panel = ref<boolean>(false)

    let panelEditar = ref<boolean>(false)
    let panelEliminar = ref<boolean>(false)
    let panelEliminarConfirmar = ref<boolean>(false)

    const abrirPanel = (interfaz: string) => {

        if(interfaz == "Editar"){

            panelEditar.value = true
            panelEliminar.value = false
            panelEliminarConfirmar.value = false
            panel.value = true

        }else if(interfaz == "Eliminar"){
      
            panelEditar.value = false
            panelEliminar.value = true
            panelEliminarConfirmar.value = false
            panel.value = true

        }else{

            panelEditar.value = false
            panelEliminar.value = false
            panelEliminarConfirmar.value = true
            panel.value = true

        }

    }

    const ocultarTodo = () => {

        panelEditar.value = false
        panelEliminar.value = false
        panelEliminarConfirmar.value = false
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