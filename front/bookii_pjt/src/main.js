// main.js

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// custom.scss import
import '@/assets/custom.scss'

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount('#app')
