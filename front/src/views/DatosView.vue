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
        <main :style="{filter : enfoque, pointerEvents : funcionamiento, overflow : barra}" class="datos">
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

    let enfoque = ref<string>('blur(0px)')
    let funcionamiento = ref<string>('all')
    let barra = ref<string>('auto')

    // Funciones

    const cambioTabla = (modelo: any) => model.value = modelo

    function interfazCreacion(interfaz: string){

        if(interfaz == 'producto'){

            newProdut.value = true
            newCategory.value = false
            newService.value = false
            enfoque.value = 'blur(7px)'
            funcionamiento.value = 'none'
            barra.value = 'hidden'

        }
        else if(interfaz == 'categoria'){

            newProdut.value = false
            newCategory.value = true
            newService.value = false
            enfoque.value = 'blur(7px)' 
            funcionamiento.value = 'none'
            barra.value = 'hidden'

        }
        else{

            newProdut.value = false
            newCategory.value = false
            newService.value = true
            enfoque.value = 'blur(7px)'
            funcionamiento.value = 'none'
            barra.value = 'hidden'

        }

    }

    function interfazOcultar(){

        newProdut.value = false
        newCategory.value = false
        newService.value = false
        enfoque.value = 'blur(0px)'
        funcionamiento.value = 'all'
        barra.value = 'auto'

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

    }

    .contenedor-enter-active, .contenedor-leave-active{

        transition: transform 0.5s ease-in-out;

    }

    .contenedor-enter-from, .contenedor-leave-to{

        transform: scale(0.1);

    }

</style>