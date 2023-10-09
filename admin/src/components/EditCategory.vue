<template>
    <div class="edit-category">
        
        <h1 class="edit-category-title"> Editar categoria </h1>
        <div class="edit-category-campo">
            <label> Nombre de la categoria:  </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
        </div>
        <div class="edit-category-button">
            <button @click="editarCategoria"> Editar </button>
        </div>

    </div>
</template>

<script setup>

    import { useStore } from '@/store/pinia';
    import { ref } from 'vue'
    import { useRoute, useRouter } from 'vue-router';

    const pinia = useStore()
    const ruta = useRoute()
    const enrutado = useRouter()

    let nombre = ref("")

    function editarCategoria(){

        let producto = pinia.listaProductos[ruta.params.id]

        fetch(`http://127.0.0.1:8000/api/Producto/${producto.id}/`, {

            method: 'PATCH',
            body: JSON.stringify({

                nombre: nombre.value,

            }),
            headers: {"content-type": "application/json"}

        });

        enrutado.push('/admin/category')

        setTimeout(() => {

            pinia.getCategorias()

        }, 600)

    }

</script>

<style lang="scss" scoped>

    .edit-category{

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

        &-button{

            width: 100%;
            height: 100%;
            display: flex;
            justify-content: flex-end;
            align-items: flex-end;

            button{

                @include botones($first-color);
                height: max-content;

            }

        }

    }

</style>