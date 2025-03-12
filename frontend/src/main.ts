import '@/style/index.scss'

import { createApp } from 'vue'
import { pinia } from "@/stores"

import App from '@/pages/IndexView.vue'

import router from './router'
import 'uno.css'

const appContainer = document.createElement('div')
appContainer.setAttribute('style', 'text-rendering: geometricPrecision;letter-spacing: -0.1px;')
document.body.appendChild(appContainer)

const app = createApp(App)

app.use(pinia)
app.use(router)

app.mount(appContainer)
