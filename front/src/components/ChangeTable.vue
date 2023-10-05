<template>
    <section class="cambiar-tabla">
        <h1> Seleccionar tabla </h1>
        <div class="cambiar-tabla-lista-tablas">
            <button @click="cambiarInformacion(productos)"> Productos </button>
            <button @click="cambiarInformacion(servicios)"> Servicios </button>
            <button @click="cambiarInformacion(categorias)"> Categorias </button>
            <button @click="cambiarInformacion(pedidos)"> Pedidos </button>
            <button @click="cambiarInformacion(usuarios)"> Usuarios </button>
        </div>
    </section>
</template>

<script lang="ts" setup>

    import { defineEmits, defineAsyncComponent } from 'vue';

    const emits = defineEmits(['changeModel'])

    const productos = defineAsyncComponent({

        loader: () => import('./ProductsInfo.vue'),
        loadingComponent: () => import('./LoaderComp.vue'),
        delay: 200,
        errorComponent: () => import('./ErrorComp.vue'),
        timeout: 3000

    })

    const servicios = defineAsyncComponent({

        loader: () => import('./ServicesInfo.vue'),
        loadingComponent: () => import('./LoaderComp.vue'),
        delay: 200,
        errorComponent: () => import('./ErrorComp.vue'),
        timeout: 3000

    })

    const categorias = defineAsyncComponent({

        loader: () => import('./CategorysInfo.vue'),
        loadingComponent: () => import('./LoaderComp.vue'),
        delay: 200,
        errorComponent: () => import('./ErrorComp.vue'),
        timeout: 3000

    })

    const pedidos = defineAsyncComponent({

        loader: () => import('./OrdersInfo.vue'),
        loadingComponent: () => import('./LoaderComp.vue'),
        delay: 200,
        errorComponent: () => import('./ErrorComp.vue'),
        timeout: 3000

    })
 
    const usuarios = defineAsyncComponent({

        loader: () => import('./UsersInfo.vue'),
        loadingComponent: () => import('./LoaderComp.vue'),
        delay: 200,
        errorComponent: () => import('./ErrorComp.vue'),
        timeout: 3000

    })

    const cambiarInformacion = (modeloSeleccionado: any) => {

        emits('changeModel', modeloSeleccionado)

    }

</script>

<style lang="scss" scoped>

    .cambiar-tabla{

        @include barras-laterales('10%');

        h1{

            text-align: center;
            color: #fff;

        }

        &-lista-tablas{

            width: 100%;
            height: max-content;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-top: 30px;

            button{

                @include botones('#fff');
                color: #000;
                font-weight: 100;
                margin: 20px 0;
                width: 80%;

            }

            button:hover{

                background: #ddd;

            }   

        }

    }

</style>