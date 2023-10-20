<template>
    <div class="edit-category" :style="{background: pinia.fondoEdits}">
        
        <h1 class="edit-category-title"> Editar categoria </h1>
        <p class="error" v-if="error"> No dejes ningun campo en blanco </p>
        <div class="edit-category-campo">
            <label> Nombre de la categoria:  </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
        </div>
        <div class="edit-category-button">
            <button :style="{background: pinia.greentheme}" @click="editarCategoria"> Editar </button>
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

    let error = ref(false)

    function editarCategoria(){

        let categoria = pinia.listaCategorias[ruta.params.id]

        if(nombre.value != ""){

            fetch(`http://127.0.0.1:8000/api/Categoria/${categoria.id}/`, {

                method: 'PATCH',
                body: JSON.stringify({

                    nombre: nombre.value,

                }),
                headers: {"content-type": "application/json"}

            });

            enrutado.push('/admin/category')

            setTimeout(() => {

                pinia.getCategorias()

            }, 1000)

        }else{

            error.value = true

        }

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
        transition: background 0.5s ease;

        &-title{

            text-align: center;
            margin-bottom: 20px;

        }

        .error{

            text-align: center;
            color: #f00;
            margin-bottom: 20px;

        }

        &-campo{

            margin-bottom: 10px;

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

                @include botones();
                height: max-content;

            }

        }

    }

</style>