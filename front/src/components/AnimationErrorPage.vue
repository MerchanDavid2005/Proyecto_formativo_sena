<template>

    <div class="animation-error">

        <v-icon class="animation-error-car" name="bi-cart-x-fill" scale="7"></v-icon>
        <div class="animation-error-floor"></div>

    </div>

</template>

<style lang="scss" scoped>

    @keyframes animationFall {

        0%{

            transform: translateX(0px);

        }

        20%{

            transform: translate(600px);

        }

        45%{

            transform: translate(1300px) translateY(300px) rotateZ(420deg);

        }

        80%{

            transform: translate(-900px) translateY(700px);

        }

        85%{

            transform: translateX(-900px) translateY(0);

        }

        100%{

            transform: translateX(0);

        }
        
    }

    .animation-error{

        width: 60%;
        height: 50%;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: flex-start;
        background: #fff;
        color: #000;
        outline: 2px solid #fff;
        border-radius: 10px;
        overflow: hidden;

        &-car{

            animation-name: animationFall;
            animation-duration: 5s;
            animation-iteration-count: infinite;
            animation-timing-function: linear;

        }

        &-floor{

            width: 60%;
            height: 40%;
            background: #444;

        }

    }

</style>