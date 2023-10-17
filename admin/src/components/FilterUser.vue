<template>
    <div class="filtrar" :style="{background: pinia.fondoFiltros}">
        
        <div>
            <label> Buscar usuario:  </label>
            <input v-model="usuario" type="text" placeholder="Usuario">
            <button :style="{background: pinia.greentheme}" @click="buscarUsuario"> Buscar </button>
            <label> Buscar nombre:  </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
            <button :style="{background: pinia.greentheme}" @click="buscarNombre"> Buscar </button>
        </div>
        <button :style="{background: pinia.greentheme}" @click="todo"> Todo </button>

    </div>
</template>

<script setup>

    import { useStore } from '@/store/pinia'
    import { ref } from 'vue'

    const pinia = useStore()

    let usuario = ref("")
    let nombre = ref("")

    const buscarUsuario = () => {

        pinia.listaUsuariosFilter = pinia.listaUsuarios.filter(

            i => i.nombre_usuario.toLowerCase().startsWith(usuario.value.toLowerCase())

        )

    }

    const buscarNombre = () => {

        pinia.listaUsuariosFilter = pinia.listaUsuarios.filter(

            i => i.nombre.toLowerCase().startsWith(nombre.value.toLowerCase())

        )

    }
    const todo = () => {

        pinia.listaUsuariosFilter = pinia.listaUsuarios
        usuario.value = ""
        nombre.value = ""

    }

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
        padding: 10px;
        border-radius: 15px;
        transition: background 0.5s ease;

        input, select{

            @include inputs();
            margin: 0 10px;
            
        }

        button{

            @include botones();
            margin: 0 10px;
            transition: background 0.5s ease;

        }

        button:focus{

            outline: 0;

        }

        label{

            margin: 0 10px;

        }

    }

</style>