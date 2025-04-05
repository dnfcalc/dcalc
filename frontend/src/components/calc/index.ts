import type { App } from "vue"
import Button from "./button/index.vue"
import Tabs from "./tabs/index.vue"
import Tab from "./tab/index.vue"
import Select from "./select/index.vue"
import Option from "./option/index.vue"
import Menu from "./menu/menu.vue"
import Checkbox from "./checkbox/index.vue"
import Collapse from "./collapse/index.vue"
import Dialog from "./dialog/index.vue"
import Tooltip from "./tooltip/index.vue"
import Iconselect from "./iconselect/index.vue"
import Selection from "./selection/index.vue"
import Slider from "./slider/index.vue"


export const components = {
  Button,
  Tabs,
  Option,
  Tab,
  Select,
  Menu,
  Checkbox,
  Collapse,
  Dialog,
  Tooltip,
  Iconselect,
  Selection,
  Slider
}

export type CalcComponents = typeof components

export function install(app: App) {
  for (const [key, value] of Object.entries(components)) {
    app.component(`calc-${key.toLocaleLowerCase()}`, value)
  }
}

export default components
