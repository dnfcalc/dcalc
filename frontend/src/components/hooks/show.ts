import type { Fn } from "@vueuse/core"
import type { InjectionKey, Ref } from "vue";
import { inject, provide, ref, watch } from "vue"

const IsOpenSymbol: InjectionKey<Ref<boolean>> = Symbol("is-open")

export function isShow() {
  return inject(IsOpenSymbol, ref(false))
}

interface OnShowOption {
  immediate?: boolean
}

export function onShow(fn: Fn, { immediate = false }: OnShowOption = {}) {
  return watch(
    isShow(),
    val => {
      if (val) {
        fn()
      }
    },
    { immediate }
  )
}

export function provideShow(ref: Ref<boolean>) {
  provide(IsOpenSymbol, ref)
}
