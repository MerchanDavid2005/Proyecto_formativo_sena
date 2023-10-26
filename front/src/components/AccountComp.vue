<template>

    <div class="cuenta">

        <div class="cuenta-foto">

            <img :src="pinia.datosUsuario.foto" :alt="pinia.datosUsuario.nombre_usuario">

        </div>

        <div class="cuenta-info">

            <div class="cuenta-info-titulo">
                <h1> ¡Hola! {{ pinia.datosUsuario.nombre_usuario }} </h1>
                <button @click="cerrarSesion" title="Cerrar sesion">
                    <v-icon name="ri-logout-box-line" scale="1.5"></v-icon>
                </button>
            </div>

            <div class="cuenta-info-dato">
                <strong style="margin:30px 0"> Informacion de tu cuenta: </strong>
                <div class="cuenta-info-dato-campo">
                    <strong> Nombre de usuario:  </strong>
                    <input v-model="usuario" type="text" :readonly="noEditar">
                </div>
                <div class="cuenta-info-dato-campo">
                    <strong> Nombre:  </strong>
                    <input v-model="nombre" type="text" :readonly="noEditar">
                </div>
                <div class="cuenta-info-dato-campo">
                    <strong> Correo:  </strong>
                    <input v-model="email" type="text" :readonly="noEditar">
                </div>
                <div v-show="!noEditar" class="cuenta-info-dato-campo">
                    <strong> Foto:  </strong>
                    <input type="file" :onchange="valorImagen">
                </div>
                <div class="cuenta-info-dato-ultimo-campo">
                    <div>
                        <button 
                            v-if="noEditar == true"  
                            @click="habilitarEditar" 
                            class="boton-editar"> Actualizar datos 
                        </button>
                        <button 
                            v-if="noEditar == false" 
                            @click="editarDatos" 
                            class="boton-editar"> Actualizar 
                        </button>
                        <button
                            v-if="noEditar == true" 
                            @click="emits('verify', 'Eliminar')"
                            class="boton-eliminar"> Eliminar cuenta 
                        </button>
                        <button
                            v-if="noEditar == false"
                            @click="desabilitarEditar"
                            class="boton-eliminar"> Cancelar
                        </button>
                    </div>
                </div>
            </div>
        </div>
        
    </div>

</template>

<script lang="ts" setup>

    import { useStore } from '../store/pinia'
    import { useRouter } from 'vue-router'; 
    import { ref, defineEmits, onMounted } from 'vue';

    const emits = defineEmits(['verify'])
    const enrutado = useRouter()
    const pinia = useStore()

    let noEditar = ref<boolean>(true)

    let usuario = ref<string>(pinia.datosUsuario.nombre_usuario)
    let nombre = ref<string>(pinia.datosUsuario.nombre)
    let email = ref<string>(pinia.datosUsuario.email)
    let foto = ref<string>(pinia.datosUsuario.foto)
    
    const cerrarSesion = () => {

        localStorage.removeItem("token")
        pinia.usuarioLogeado = false
        enrutado.push('/')
        pinia.datosUsuario = {

            id: 1,
            nombre_usuario: "Anonimo",
            nombre: "Anonimo",
            email: "Anomimo@gmail.com",
            foto: "http://127.0.0.1:8000/media/usuarios/default.png",
            password: "Anonimo",
            rol: "Cliente",
            carrito: []

        }

    }

    const habilitarEditar = () => noEditar.value = false

    const desabilitarEditar = () => {

        usuario.value = pinia.datosUsuario.nombre_usuario
        nombre.value = pinia.datosUsuario.nombre
        email.value = pinia.datosUsuario.email

        noEditar.value = true

    }

    const valorImagen = (img: any) => foto.value = img.target.files[0]

    const editarDatos = () => {

        pinia.datosUsuarioEditar = {

            id: pinia.datosUsuario.id,
            nombre_usuario: usuario.value,
            nombre: nombre.value,
            email: email.value,
            foto: foto.value,
            password: pinia.datosUsuario.password,
            rol: "Cliente",
            carrito: pinia.datosUsuario.carrito

        }

        emits('verify', 'Editar')

    }

    if(pinia.usuarioLogeado == false){

        enrutado.push('/')

    }

    onMounted(() => {
        
        pinia.getPedidos()

    })

</script>

<style lang="scss" scoped>

    .cuenta{

        width: 85%;
        height: 70%;
        display: flex;
        justify-content: space-around;
        margin-bottom: 10vh;

        &-foto{

            display: flex;
            justify-content: center;
            align-self: center;
            width: 30%;
            height: 100%;

            img{

                object-fit: cover;
                clip-path: circle(50%);

            }

        }

        &-info{

            width: 60%;
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            
            &-titulo{

                width: 100%;
                height: max-content;
                display: flex;
                justify-content: space-between;

                h1{

                    font-size: 50px;

                }

                button{

                    @include botones($fondo-boton-eliminar);

                }

            }

            &-dato{

                width: 100%;
                height: max-content;
                display: flex;
                flex-direction: column;
                align-items: flex-start;

                input{

                    @include inputs();
                    width: 45%;

                }
                    
                &-campo{

                    width: 100%;
                    height: max-content;
                    justify-content: space-between;

                }

                &-ultimo-campo{

                    width: 100%;
                    height: max-content;
                    display: flex;
                    justify-content: flex-end;
                    align-items: center;

                    .boton-editar{

                        @include botones($fondo-boton-crear);
                        margin-right: 10px; 

                    }   

                    
                    .boton-eliminar{

                        @include botones($fondo-boton-eliminar);

                    }

                }

            }

        }

    }

</style>
