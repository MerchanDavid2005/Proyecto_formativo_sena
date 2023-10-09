<template>
    <div class="select-category">
        
        <h1 class="select-category-title"> Servicio sin editar </h1>
        <div class="select-category-campo">
            <label> Nombre del servicio:  </label>
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

        height: 30%;
        width: 30%;
        display: flex;
        flex-direction: column;
        outline: 2px solid #000;
        border-radius: 15px;
        padding: 15px;

        &-title{

            text-align: center;
            margin: 40px;

        }

        &-campo{

            margin-bottom: 20px;

            input, textarea, select{

                @include inputs();

            }

        }

    }

</style>