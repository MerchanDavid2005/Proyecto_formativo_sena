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
        height: 90%;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        background: transparent;
        position: absolute;
        z-index: 10000000;
        top: 0;

        @for $i from 1 through 7{

            div:nth-child(#{$i}){

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