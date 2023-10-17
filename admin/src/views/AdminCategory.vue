<template>

  <AdminDefault>

    <div :class="{'category-body': !advertencia, 'category-body-none': advertencia}">

      <h1 class="category-body-title"> Categorias </h1>
      <CategorysAll @eliminar="mostrar" />

    </div>

    <div class="interfaz">

      <transition name="transicionCategoryDanger">

        <DeleteConfirm 
          @cerrar="ocultar" 
          v-show="advertencia" 
          modelo="Categoria" 
          registro="esta categoria" />

      </transition>

    </div>

  </AdminDefault>
  
</template>

<script setup>

  import AdminDefault from '@/layouts/adminDefault.vue'
  import CategorysAll from '@/components/CategorysAll.vue';
  import DeleteConfirm from '@/components/DeleteConfirm.vue';

  import { ref } from 'vue';
  import { useRouter } from 'vue-router';

  const enrutado = useRouter()

  let advertencia = ref(false)

  const mostrar = () => advertencia.value = true

  const ocultar = () => advertencia.value = false

  if(localStorage.getItem('token') == "Error" || localStorage.getItem("token") == null){

    enrutado.push('/')

  }

</script>

<style lang="scss" scoped>

  .category-body{

    width: 100%;
    height: 100%;
    padding: 2%;
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

  .category-body-none{

    width: 100%;
    height: 100%;
    padding: 2%;
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

  .transicionCategoryDanger-enter-active, .transicionCategoryDanger-leave-active{

    transition: all 2s cubic-bezier(1, -0.3, 0, 1.2);

  }

  .transicionCategoryDanger-enter-from, .transicionCategoryDanger-leave-to{

    transform: translateY(-800px);

  }

</style>
