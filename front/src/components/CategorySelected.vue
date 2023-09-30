<template>
    <article class="category-selected">
        <h1> Categoria sin editar </h1>
        <div>
            <label> Nombre de la categoria: </label>
            <input type="text" :value="nombre" readonly>
        </div>
    </article>
</template>

<script lang="ts" setup>

    import { useRoute } from 'vue-router';
    import { onMounted, ref } from 'vue';

    const route = useRoute()

    let nombre = ref<string>("")

    onMounted(() => {

        fetch(`http://127.0.0.1:8000/api/Categoria/${route.params.id}/`)
            .then(res => res.json())
            .then(info => {

                nombre.value = info.nombre

            })

    })

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

    }

</style>

