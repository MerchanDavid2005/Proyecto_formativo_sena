<template>

  <AdminDefault>

    <div :class="{'products-body' : !advertencia, 'products-body-none' : advertencia}">

      <h1 class="products-body-title"> Productos </h1>
      <FilterProduct />
      <ProductsAll @eliminar="mostrar" />

    </div>

    <div class="interfaz">

      <transition name="transicionProductDanger">

        <DeleteConfirm 
          @cerrar="ocultar" 
          v-show="advertencia" 
          modelo="Producto" 
          registro="este producto" />
          
      </transition>
    
    </div>

  </AdminDefault>
  
</template>

<script setup>

  import AdminDefault from '@/layouts/adminDefault.vue'
  import ProductsAll from '@/components/ProductsAll.vue';
  import FilterProduct from '@/components/FilterProduct.vue'
  import DeleteConfirm from '@/components/DeleteConfirm.vue';
  import jwt_decode from 'jwt-decode'

  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { useStore } from '@/store/pinia'

  const pinia = useStore();
  const enrutado = useRouter()

  let advertencia = ref(false)

  const mostrar = () => advertencia.value = true

  const ocultar = () => advertencia.value = false

  if(localStorage.getItem('token') == "Error" || localStorage.getItem("token") == null){

    enrutado.push('/');

  }else{

    const tokenDecodificado = jwt_decode(localStorage.getItem("token"));
    pinia.getUsuario(tokenDecodificado.id);

  }



</script>

<style lang="scss" scoped>

  .products-body{

    width: 100%;
    height: 100%;
    padding: 2%;
    display: flex;
    flex-direction: column;
    filter: brightness(100%);
    background: transparent;
    pointer-events: all;
    overflow: auto;
    position: static;
    z-index: 1000;
    transition: all 0.5s ease-in-out;

    &-title{

      font-size: 50px;
      margin-bottom: 10vh;
      text-align: center;

    } 

  }

  .products-body-none{

    width: 100%;
    height: 100%;
    padding: 2%;
    display: flex;
    flex-direction: column;
    filter: brightness(20%);
    background: #444;
    pointer-events: none;
    overflow: hidden;
    position: static;
    z-index: 1000;
    transition: all 0.5s ease-in-out;

  }

  .interfaz{

    width: 100%;
    height: 90%;
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;

  }

  .transicionProductDanger-enter-active, .transicionProductDanger-leave-active{

    transition: all 2s cubic-bezier(1, -0.3, 0, 1.2);

  }

  .transicionProductDanger-enter-from, .transicionProductDanger-leave-to{

    transform: translateY(-800px);

  }

</style>
