import { h, reactive, renderList } from "vue"
import { createSharedComposable } from "@vueuse/core"
import ActionDialog from "@/components/calc/action-dialog/index.vue"
import type { JSX } from "vue/jsx-runtime"

export type ConfirmDialogOption = Omit<ShowDialogOption, "okButton" | "cancelButton">
export type AlertDialogOption = Omit<ShowDialogOption, "okButton" | "cancelButton">
export type ElementLike = JSX.Element | string | ElementLike[]

function randomId() {
  return Symbol(Math.random().toString(36).slice(2, 9))
}

type DialogID = string | number | symbol

export interface ShowDialogOption {
  id?: DialogID
  /**
   * 标题
   */
  header?: string | boolean
  /**
   * 内容插槽
   */
  content?: (() => ElementLike) | ElementLike
  /**
   * 操作区插槽
   */
  action?: (() => ElementLike) | ElementLike

  cache?: boolean

  /**
   * 超时自动关闭
   */
  timeout?: number

  /**
   * 关闭时的延迟动画
   */
  duration?: number

  /**
   * 确定按钮文本 为false时不显示
   */
  okButton?: string | boolean
  /**
   * 取消按钮文本 为false时不显示
   */
  cancelButton?: string | boolean
  /**
   * 拒绝按钮文本 为false时不显示
   */
  rejectButton?: string | boolean

  // 默认状态
  defaultStatus?: DialogResult["status"]

  mask?: boolean

  scale?: number
}

export interface DialogInstance {
  id?: DialogID
  visible: boolean
  render: (visible?: boolean) => ElementLike
  resolve: (result: DialogResult) => void
}

export interface DialogResult {
  id: DialogID
  status: "ok" | "reject" | "cancel" | "none"
  data?: any
  readonly isOk: boolean
  readonly isCancel: boolean
  readonly isReject: boolean
}

export const useDialog = createSharedComposable(() => {
  const dialogs = reactive(new Map<DialogID, DialogInstance>())

  // 注册窗口
  function open(dialog: DialogInstance) {
    const id = dialog.id ?? randomId()
    dialogs.set(id, dialog)
    return id
  }

  function close(id: DialogID, status = "cancel", duration = 400) {
    const dialog = dialogs.get(id)
    if (!dialog) {
      return
    }
    dialog.resolve({
      id,
      status: "ok",
      get isOk() {
        return status == "ok"
      },
      get isCancel() {
        return status == "cancel"
      },
      get isReject() {
        return status == "reject"
      }
    })
    dialog.visible = false
    const fn = () => dialogs.delete(id)
    if (duration > 0) {
      setTimeout(fn, duration)
    } else {
      fn()
    }
  }

  function render() {
    return renderList(dialogs.values(), e => e.render(e.visible))
  }

  async function show(option: ShowDialogOption = {}) {
    return new Promise<DialogResult>(resolve => {
      const { id = randomId(), header = true, content, action, timeout, okButton = false, cancelButton = false, rejectButton = false, defaultStatus = "none", duration = 400, mask = false, scale = 1.0 } = option

      const onClose = (status: DialogResult["status"] = defaultStatus) => {
        close(id, status, duration)
      }

      open({
        id,
        visible: true,
        resolve,
        render(visible = true) {
          return h(
            ActionDialog,
            {
              header,
              okButton,
              cancelButton,
              rejectButton,
              visible,
              onClose,
              mask,
              scale
            },
            {
              default() {
                switch (typeof content) {
                  case "function":
                    return content()
                  case "string":
                    return h("div", { class: "w-full justify-center text-hex-d4d6b6 text-center", style: "margin:10px" }, content)
                  default:
                    return content
                }
              },
              action: typeof action == "function" || !action ? action : () => action
            }
          )
        }
      })

      if (timeout) {
        setTimeout(onClose, timeout)
      }
    })
  }

  async function alert(option: AlertDialogOption = {}) {
    return show({
      ...option,
      defaultStatus: "ok",
      okButton: true,
      cancelButton: false
    })
  }

  async function confirm(option: ConfirmDialogOption = {}) {
    return show({
      ...option,
      defaultStatus: "cancel",
      okButton: true,
      cancelButton: true
    })
  }
  return {
    confirm,
    alert,
    render,
    show,
    close,
    randomId
  }
})
