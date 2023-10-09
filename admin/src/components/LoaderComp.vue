<template>
    <div class="animation-load">
        
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>

    </div>
</template>

<style lang="scss" scoped>

    .animation-load{

        width: 100%;
        height: 90vh;
        display: flex;
        justify-content: center;
        overflow: hidden;
        background: #666;
        position: absolute;
        z-index: 10000000;
        top: 0;

        @for $i from 1 through 7{

            div:nth-child(#{$i}){

                top: 25%;
                position: absolute;
                border-radius: 100%;
                background: #000;
                width: 70px;
                height: 70px;
                transform: translateY(130px) rotateZ($i * 50deg) translateX(130px);
                animation-name: colores;
                animation-duration: 1.5s;
                animation-iteration-count: infinite;
                animation-fill-mode: forwards;
                animation-delay: $i * 0.2s;
    
            }

            @keyframes colores {
                
                0%{

                    background: #000;

                }

                100%{

                    background: #fff;

                }

            }

        }

    }

</style>