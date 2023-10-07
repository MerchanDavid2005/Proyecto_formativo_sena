<template>
    <div class="filtrar">
        
        <div>
            <label> Buscar servicio:  </label>
            <input v-model="servicio" type="text" placeholder="Nombre servicio">
            <button @click="buscarServicio"> Buscar </button>
            <label> Filtrar por precio:  </label>
            <label> Mayor precio: </label>
            <input v-model="precio" type="radio" name="precio" value="Mayor precio">
            <label> Menor precio: </label>
            <input v-model="precio" type="radio" name="precio" value="Menor precio">
        </div>
        <button @click="todo"> Todo </button>

    </div>
</template>

<script setup>

    import { useStore } from '@/store/pinia'
    import { ref, watch } from 'vue'

    const pinia = useStore()

    let servicio = ref("")
    let precio = ref("")

    const todo = () => {

        pinia.listaServiciosFilter = pinia.listaServicios
        servicio.value = ""
        precio.value = "Mayor precio"

    }

    const buscarServicio = () => {

        pinia.listaServiciosFilter = pinia.listaServicios.filter(

            i => i.nombre.toLowerCase().startsWith(servicio.value.toLowerCase())

        )

    }

    watch(precio, () => {

       if(precio.value == "Mayor precio"){

            pinia.listaServiciosFilter = pinia.listaServiciosFilter.sort(
                
                (a, b) => a.precio - b.precio
            
            )

        }else{

            pinia.listaServiciosFilter = pinia.listaServiciosFilter.sort(
                
                (a, b) => b.precio - a.precio
            
            )

        }

    })

</script>

<style lang="scss" scoped>

    .filtrar{

        width: 100%;
        height: max-content;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #fff;
        margin: 0 0 30px 0;
        background: $second-color;
        padding: 10px;
        border-radius: 15px;

        input, select{

            @include inputs();
            margin: 0 10px;
            
        }

        button{

            @include botones($first-color);
            margin: 0 10px;

        }

        button:focus{

            outline: 0;

        }

        label{

            margin: 0 10px;

        }

    }

</style>