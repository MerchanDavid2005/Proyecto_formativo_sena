<template>
    <article class="category-selected">
        <h1> Editar categoria </h1>
        <div>
            <label> Nombre de la categoria: </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
        </div>
        <div class="contenedor-botones">
            <button @click="limpiar"> Limpiar </button>
            <router-link class="boton-actualizar" :to="{name: 'datos'}">
                <button @click="actualizar"> Actualizar </button>
            </router-link>
        </div>
    </article>
</template>

<script lang="ts" setup>

    import { useRoute } from 'vue-router';
    import { useStore } from '../store/pinia';
    import { ref } from 'vue';

    const pinia = useStore()
    const route = useRoute()

    let nombre = ref<string>("")

    const limpiar = () => nombre.value = ""

    const actualizar = () => {

        fetch(`http://127.0.0.1:8000/api/Categoria/${route.params.id}/`, {

            method: 'PUT',
            body: JSON.stringify({

                nombre: nombre.value,

            }),
            headers: {"content-type" : "application/json"}
                
        })

        setTimeout(() => {

            pinia.getServicios()
            limpiar()

        }, 500)

    }

</script>

<style lang="scss" scoped>

    .category-selected{

        width: 30%;
        height: 30%;
        padding: 15px;
        background: #fff;
        outline: 2px solid #000;
        border-radius: 10px;

        h1{

            text-align: center;
            margin: 20px 0;
            font-size: 25px;

        }

        div{

            margin: 10px 0;

            input{

                @include inputs();
    
            }
    

        }

        .contenedor-botones{

            display: flex;
            justify-content: space-evenly;
            margin: 5vh 0;

            button{

                @include botones($fondo-boton-limpiar);
                width: 40%;

            }

            .boton-actualizar{

                width: 40%;
                text-decoration: none;
                color: #fff;

                button{

                    @include botones($fondo-boton-crear);
                    width: 100%;

                }

            }

        }

    }

</style>

