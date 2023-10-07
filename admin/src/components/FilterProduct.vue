<template>
    <div class="filtrar">
        
        <div>
            <label> Buscar producto:  </label>
            <input v-model="producto" type="text" placeholder="Nombre producto">
            <button @click="buscarProducto"> Buscar </button>
            <label> Filtrar por categoria:  </label>
            <select v-model="categoria">
                <option value="Todo">
                    Todo
                </option>
                <option 
                    v-for="(cate, i) in pinia.listaCategorias" 
                    :value="cate.nombre"
                    :key="i">
                    
                    {{ cate.nombre }}
    
                </option>
            </select>
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

    let producto = ref("")
    let precio = ref("")
    let categoria = ref("Todo")

    const todo = () => {

        pinia.listaProductosFilter = pinia.listaProductos
        producto.value = ""
        precio.value = "Mayor precio"
        categoria.value = "Todo"

    }

    const buscarProducto = () => {

        pinia.listaProductosFilter = pinia.listaProductos.filter(

            i => i.nombre.toLowerCase().startsWith(producto.value.toLowerCase())

        )

    }

    watch(precio, () => {

       if(precio.value == "Mayor precio"){

            pinia.listaProductosFilter = pinia.listaProductosFilter.sort(
                
                (a, b) => a.precio - b.precio
            
            )

        }else{

            pinia.listaProductosFilter = pinia.listaProductosFilter.sort(
                
                (a, b) => b.precio - a.precio
            
            )

        }

    })

    watch(categoria, () => {

        if(categoria.value == "Todo"){

            pinia.listaProductosFilter = pinia.listaProductos
            precio.value = "Mayor precio"

        }else{

            pinia.listaProductosFilter = pinia.listaProductos.filter(

                i => i.categoria == categoria.value

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