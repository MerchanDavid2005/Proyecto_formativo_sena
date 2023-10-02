import { createApp } from 'vue'
import { createPinia } from 'pinia'

const pinia = createPinia()

import App from './App.vue'
import router from './router'

import { OhVueIcon, addIcons } from "oh-vue-icons";
import { MdHomeRound, FaDatabase, BiCartFill, MdWorkSharp, MdContactmail, MdLightmode, MdDarkmode, MdChangecircleRound, MdDelete, BiArrowLeftShort, BiCartPlusFill, BiCartCheckFill, BiCartXFill } from "oh-vue-icons/icons";

addIcons( MdHomeRound, FaDatabase, BiCartFill, MdWorkSharp, MdContactmail, MdLightmode, MdDarkmode, MdChangecircleRound, MdDelete, BiArrowLeftShort, BiCartPlusFill, BiCartCheckFill, BiCartXFill );

createApp(App).use(router).use(pinia).component("v-icon", OhVueIcon).mount('#app')
