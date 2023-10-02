<template>
    <MainDefault>
        <div class="contenedores-creadores">
            <transition name="contenedor">
                <NewProduct
                    v-show="newProdut" 
                    @ocultarInterfaz="interfazOcultar" 
                />
            </transition>

            <transition name="contenedor">
                <NewService 
                    v-show="newService"
                    @ocultarInterfaz="interfazOcultar"
                />
            </transition>

            <transition name="contenedor">
                <NewCategory 
                    v-show="newCategory"
                    @ocultarInterfaz="interfazOcultar"
                />
            </transition>
        </div>
        <main :class="{'datos': funcionando, 'datos-none' : !funcionando}">
            <ChangeTable @changeModel="cambioTabla" />
            <component 
                :is="model" 
                @mostrarInterfaz="interfazCreacion" />
            <FilterData />
        </main>
    </MainDefault>
</template>

<script lang="ts" setup>

    // Importaciones

    import MainDefault from '../layouts/MainDefault.vue'
    import ChangeTable from '../components/ChangeTable.vue';
    import FilterData from '../components/FilterData.vue'
    import NewProduct from '../components/NewProduct.vue';
    import NewService from '../components/NewService.vue';
    import NewCategory from '../components/NewCategory.vue';

    // Variables
    
    import { shallowRef, defineAsyncComponent, ref } from 'vue';

    const productos = defineAsyncComponent(() => import('../components/ProductsInfo.vue'))

    let model = shallowRef(productos)

    let newProdut = ref<boolean>(false)
    let newCategory = ref<boolean>(false)
    let newService = ref<boolean>(false)

    let funcionando = ref<boolean>(true)

    // Funciones

    const cambioTabla = (modelo: any) => model.value = modelo

    function interfazCreacion(interfaz: string){

        if(interfaz == 'producto'){

            newProdut.value = true
            newCategory.value = false
            newService.value = false

            funcionando.value = false
 
        }
        else if(interfaz == 'categoria'){

            newProdut.value = false
            newCategory.value = true
            newService.value = false

            funcionando.value = false

        }
        else{

            newProdut.value = false
            newCategory.value = false
            newService.value = true

            funcionando.value = false

        }

    }

    function interfazOcultar(){

        newProdut.value = false
        newCategory.value = false
        newService.value = false

        funcionando.value = true

    }

</script>

<style lang="scss" scoped>

    .contenedores-creadores{

        width: 100%;
        height: 85vh;
        position: absolute;
        display: flex;
        align-items: center;
        justify-content: center;

    }

    .datos{

        width: 100%;
        height: 85vh;
        display: flex;
        justify-content: space-around;
        transition: filter 0.5s ease-in-out;
        padding-top: 5vh;
        filter: blur(0);
        overflow: auto;
        pointer-events: all;

    }

    .datos-none{

        width: 100%;
        height: 85vh;
        display: flex;
        justify-content: space-around;
        transition: filter 0.5s ease-in-out;
        padding-top: 5vh;
        filter: blur(7px);
        overflow: hidden;
        pointer-events: none;

    }

    .contenedor-enter-active, .contenedor-leave-active{

        transition: transform 0.5s ease-in-out;

    }

    .contenedor-enter-from, .contenedor-leave-to{

        transform: scale(0.1);

    }

</style>