<template>
    <div class="navTop">

        <div class="navTop-panel">

            <button>
                <v-icon name="md-reorder-twotone" scale="1.5"></v-icon>
            </button>

        </div>

        
        <div class="navTop-title">

            <h1> Serviteca admin </h1>

        </div>

        <div class="navTop-urls">

            <ul>

                <router-link 
                    class="navTop-urls-url" 
                    to="/admin/product">
                    <v-icon name="bi-box-seam" scale="1.5"></v-icon>
                    Productos
                </router-link>
                <router-link 
                    class="navTop-urls-url" 
                    to="/admin/category">
                    <v-icon name="md-category" scale="1.5"></v-icon>
                    Categorias 
                </router-link>
                <router-link 
                    class="navTop-urls-url" 
                    to="/admin/service">
                    <v-icon name="md-homerepairservice" scale="1.5"></v-icon>
                    Servicios
                </router-link>
                <router-link 
                    class="navTop-urls-url" 
                    to="/admin/product">
                    <v-icon name="bi-bag-check-fill" scale="1.5"></v-icon>
                    Pedidos
                </router-link>
                <router-link 
                    class="navTop-urls-url" 
                    to="/admin/product">
                    <v-icon name="fa-users" scale="1.5"></v-icon>
                    Usuarios
                </router-link>

            </ul>

        </div>
        
    </div>
</template>

<style lang="scss" scoped>

    .navTop{

        width: 100%;
        height: 10%;
        display: flex;
        justify-content: space-around;
        align-items: center;
        background: $second-color;

        &-title{

            width: 30%;
            height: 60%;
            display: flex;
            justify-content: center;
            align-items: center;
            border-left: 2px solid #fff;

            h1{

                font-size: 30px;
                color: #fff;

            }

        }

        &-urls{

            width: 60%;
            height: 60%;
            border-left: 2px solid #fff;

            ul{

                width: 100%;
                height: 100%;
                list-style: none;
                display: flex;
                justify-content: space-evenly;
                align-items: center;

                .navTop-urls-url{

                    height: 100%;
                    text-decoration: none;
                    color: #fff;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: space-between;

                }

                .navTop-urls-url:hover{

                    color: #444;

                }

            }

        }

        &-panel{

            width: 5%;
            height: 60%;
            display: flex;
            justify-content: center;
            align-items: center;

            button{

                @include botones('transparent')

            }

        }
            
    }

</style>