<template>
    <div class="select-category" :style="{background: pinia.fondoEdits}">
        
        <h1 class="select-category-title"> Categoria sin editar </h1>
        <div class="select-category-campo">
            <label> Nombre de la categoria:  </label>
            <input v-model="nombre" type="text" readonly>
        </div>

    </div>
</template>

<script setup>

    import { useStore } from '@/store/pinia';
    import { ref, onMounted } from 'vue'
    import { useRoute } from 'vue-router';

    const pinia = useStore()
    const ruta = useRoute()

    let nombre = ref("")

    onMounted(() => {

        nombre.value = pinia.listaCategorias[ruta.params.id].nombre

    })

</script>

<style lang="scss" scoped>

    .select-category{

        height: 35%;
        width: 30%;
        display: flex;
        flex-direction: column;
        outline: 2px solid #000;
        border-radius: 15px;
        padding: 15px;
        transition: background 0.5s ease;

        &-title{

            text-align: center;
            margin-bottom: 20px;

        }

        &-campo{

            margin-bottom: 10px;

            input, textarea, select{

                @include inputs();

            }

        }

    }

    @media(max-width: 1400px){

        .select-category{

            width: 45%;

        }

    }

</style>