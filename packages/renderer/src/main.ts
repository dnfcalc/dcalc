import { createApp } from "vue"
import router from "./router"
import { pinia } from "./store"
import App from "@/pages/index.vue"

import "uno.css"

import "@curev/sprite.css"

import "./app.scss"
import "./char-img.scss"

if (!window.removeLoading) {
  window.removeLoading = () => {}
}

const appContainer = document.createElement("div")

if (!window.pywebview) {
  appContainer.setAttribute("style", "text-rendering: geometricPrecision;letter-spacing: -0.1px;")
}

document.body.appendChild(appContainer)

createApp(App).use(pinia).use(router).mount(appContainer)

setTimeout(window.removeLoading, 1500)

// console.log('fs', window.fs)
// console.log('ipcRenderer', window.pywebview)

// Usage of ipcRenderer.on
// window.pywebview.on("main-process-message", (_event, ...args) => {
//   console.log("[Receive Main-process message]:", ...args);
// });
