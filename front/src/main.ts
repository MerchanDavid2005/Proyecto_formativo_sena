import { createApp } from 'vue'
import { createPinia } from 'pinia'

const pinia = createPinia()

import App from './App.vue'
import router from './router'

import { OhVueIcon, addIcons } from "oh-vue-icons";
import { MdHomeRound, BiCartFill, MdWorkSharp, MdContactmail, MdLightmode, MdDarkmode, MdChangecircleRound, MdDelete, BiArrowLeftShort, BiCartPlusFill, BiCartCheckFill, BiCartXFill, BiBagCheckFill, BiCheckCircleFill, BiArrowDownSquareFill, RiLogoutBoxLine } from "oh-vue-icons/icons";

addIcons( MdHomeRound, BiCartFill, MdWorkSharp, MdContactmail, MdLightmode, MdDarkmode, MdChangecircleRound, MdDelete, BiArrowLeftShort, BiCartPlusFill, BiCartCheckFill, BiCartXFill, BiBagCheckFill, BiCheckCircleFill, BiArrowDownSquareFill, RiLogoutBoxLine );

createApp(App).use(router).use(pinia).component("v-icon", OhVueIcon).mount('#app')
