<template>
    <div class="filtrar" :style="{background: pinia.fondoFiltros}">
        
        <div>
            <label> Buscar usuario:  </label>
            <input v-model="usuario" type="text" placeholder="Nombre usuario">
            <button :style="{background: pinia.greentheme}" @click="buscarUsuario"> Buscar </button>
            <label> Buscar producto:  </label>
            <input v-model="producto" type="text" placeholder="Nombre producto">
            <button :style="{background: pinia.greentheme}" @click="buscarProducto"> Buscar </button>
            <label> Filtrar por fecha:  </label>
            <select v-model="fecha">
                <option value="0"> Todo </option>
                <option v-for="(data, i) in fechas" :key="i" :value="data.id">
                    {{ data.nombre }}
                </option>
            </select>
        </div>
        <button :style="{background: pinia.greentheme}" @click="todo"> Todo </button>

    </div>
</template>

<script setup>

    import { useStore } from '@/store/pinia'
    import { ref, watch } from 'vue'

    const pinia = useStore()

    let usuario = ref("")
    let producto = ref("")
    let fecha = ref("0")

    let fechas = ref([

        { "id": 1, "nombre": "Enero"},
        { "id": 2,"nombre": "Febrero"},
        { "id": 3, "nombre": "Marzo" },
        { "id": 4, "nombre": "Abril" },
        { "id": 5, "nombre": "Mayo" },
        { "id": 6, "nombre": "Junio" },
        { "id": 7, "nombre": "Julio" },
        { "id": 8, "nombre": "Agosto" },
        { "id": 9, "nombre": "Septiembre" },
        { "id": 10, "nombre": "Octubre" },
        { "id": 11, "nombre": "Noviembre" },
        { "id": 12, "nombre": "Diciembre" },

    ])

    const buscarUsuario = () => {

        pinia.listaPedidosFilter = pinia.listaPedidos.filter(

            i => i.nombre.toLowerCase().startsWith(usuario.value.toLowerCase())

        )

    }

    const buscarProducto = () => {

        let arrayOrdenado = []

        if(producto.value != ""){

            pinia.listaPedidos.forEach(element => {

                for(let i of element.lista_productos){

                    if(i.nombre.toLowerCase().startsWith(producto.value.toLowerCase())){

                        arrayOrdenado.push(element)

                    }

                }

            })

            pinia.listaPedidosFilter = arrayOrdenado

        }else{

            pinia.listaPedidosFilter = pinia.listaPedidos

        }

    }

    watch(fecha, () => {

        if(fecha.value == 0){

            pinia.listaPedidosFilter = pinia.listaPedidos

        }else{

            pinia.listaPedidosFilter = pinia.listaPedidos.filter(

                i => i.fecha.slice(5, 7) == fecha.value 

            )

        }

    })

    const todo = () => {

        pinia.listaPedidosFilter = pinia.listaPedidos
        usuario.value = ""
        producto.value = ""
        fecha.value = "0"

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