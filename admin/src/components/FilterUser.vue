<template>
    <div class="filtrar">
        
        <div>
            <label> Buscar usuario:  </label>
            <input v-model="usuario" type="text" placeholder="Usuario">
            <button @click="buscarUsuario"> Buscar </button>
            <label> Buscar nombre:  </label>
            <input v-model="nombre" type="text" placeholder="Nombre">
            <button @click="buscarNombre"> Buscar </button>
            <label> Filtrar por email:  </label>
            <select v-model="email">
                <option value="Todo"> Todo </option>
                <option v-for="(mail, i) in direccionesCorreos" :key="i" :value="mail.extension">
                    {{ mail.nombre }}
                </option>
            </select>
        </div>
        <button @click="todo"> Todo </button>

    </div>
</template>

<script setup>

    import { useStore } from '@/store/pinia'
    import { ref, watch } from 'vue'

    const pinia = useStore()

    let usuario = ref("")
    let nombre = ref("")
    let email = ref("Todo")

    let direccionesCorreos = ref([

        { "nombre": "Gmail", "extension": "@gmail.com"},
        { "nombre": "Outlook", "extension": "@outlook.com"},
        { "nombre": "Yahoo", "extension": "@yahoo.com"},
        { "nombre": "AOL", "extension": "@aol.com"},
        { "nombre": "iCloud Mail", "extension": "@icloud.com"},
        { "nombre": "ProtonMail", "extension": "@protonmail.com"},
        { "nombre": "Yandex", "extension": "@yandex.ru"},
        { "nombre": "Zoho", "extension": "@zoho.com"},
        { "nombre": "Mail.com", "extension": "@mail.com"},
        { "nombre": "Tutanota", "extension": "@tutanota.com"},
        { "nombre": "Apple", "extension": "@me.com"},
  

    ])

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

    watch(email, () => {

        if(email.value == "Todo"){

            pinia.listaUsuariosFilter = pinia.listaUsuarios

        }else{

            pinia.listaUsuariosFilter = pinia.listaUsuarios.filter(

                i => i.email.toLowerCase().endsWith(email.value.toLowerCase())

            )

        }

    })

    const todo = () => {

        pinia.listaUsuariosFilter = pinia.listaUsuarios
        usuario.value = ""
        nombre.value = ""
        email.value = "Todo"

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