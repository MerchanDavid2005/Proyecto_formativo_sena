<template>
    <div class="register">

        <div :class="{'register-fondo': !codigo, 'register-fondo-none': codigo}"></div>

        <div class="register-panel">

            <transition name="panelCodigo">
            
                <CodeVerify v-show="codigo" />

            </transition>

        </div>
        
        <div :class="{'register-body': !codigo, 'register-body-none': codigo}">

            <RegisterComp @mostrarCodigo="mostrarPanelCode" />

        </div>

    </div>
</template>

<script setup>

    import RegisterComp from '@/components/RegisterComp.vue';
    import CodeVerify from '@/components/CodeVerify.vue';

    import { ref } from 'vue';

    let codigo = ref(false)

    const mostrarPanelCode = () => codigo.value = true

</script>

<style lang="scss" scoped>

    .register{

        width: 100%;
        height: 100vh;

        &-fondo{

            width: 100%;
            height: 100vh;
            position: absolute;
            background: url(https://laadministracionelectronica.files.wordpress.com/2014/10/fondo1.jpg);
            filter: blur(4px);
            background-repeat: no-repeat;
            background-size: 100%;

        }

        &-fondo-none{

            width: 100%;
            height: 100vh;
            position: absolute;
            background: url(https://laadministracionelectronica.files.wordpress.com/2014/10/fondo1.jpg);
            filter: blur(4px) brightness(20%);
            background-repeat: no-repeat;
            background-size: 100%;

        }

        &-panel{

            width: 100%;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: absolute;

        }

        &-body{

            width: 100%;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: static;

        }

        .register-body-none{

            width: 100%;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: static;
            z-index: 10;
            filter: brightness(20%);
            pointer-events: none;
    
        }

    }

    .panelCodigo-enter-active, .panelCodigo-leave-active{

        transition: transform 1s ease;

    }

    .panelCodigo-enter-from, .panelCodigo-leave-to{

        transform: scale(0.1);

    }


</style>