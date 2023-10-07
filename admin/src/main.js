import { createApp } from 'vue'
import { createPinia } from 'pinia';
import App from './App.vue'
import router from './router'

const pinia = createPinia()

import { OhVueIcon, addIcons } from "oh-vue-icons";
import { MdReorderTwotone, BiBoxSeam, MdCategory, MdHomerepairservice, BiBagCheckFill, FaUsers, MdModeeditoutline, RiDeleteBack2Fill, MdDeleteforever } from "oh-vue-icons/icons";

addIcons(MdReorderTwotone, BiBoxSeam, MdCategory, MdHomerepairservice, BiBagCheckFill, FaUsers, MdModeeditoutline, RiDeleteBack2Fill, MdDeleteforever );

createApp(App).use(router).use(pinia).component("v-icon", OhVueIcon).mount('#app')
