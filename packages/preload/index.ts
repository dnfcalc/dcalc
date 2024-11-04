import { ipcRenderer } from "electron"
import { useLoading } from "./loading"

const { appendLoading, removeLoading } = useLoading()
window.removeLoading = removeLoading
window.pywebview = {
  api: ipcRenderer
}
// window.sharedObject = {
//   storage: "test"
// }

/** docoment ready */
function domReady(condition: DocumentReadyState[] = ["complete", "interactive"]) {
  return new Promise(resolve => {
    if (condition.includes(document.readyState)) {
      resolve(true)
    } else {
      document.addEventListener("readystatechange", () => {
        if (condition.includes(document.readyState)) {
          resolve(true)
        }
      })
    }
  })
}

domReady().then(appendLoading)
