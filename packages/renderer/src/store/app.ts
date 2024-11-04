import api from "@/api";
import { decrypt, getSession } from "@/utils";
import { asyncComputed } from "@vueuse/core";
import { defineStore } from "pinia";
import { computed, ref } from "vue";

export const useAppStore = defineStore("app", () => {
  const title = ref<string>("DNF计算器 & Colg");
  const uid = ref(-1);
  const id = ref<number>();
  const head = ref<boolean>(false);
  const m_mode = ref<boolean>(true);
  const tryChange = ref<boolean>(false);
  const relesh = ref<number>(0);

  window.addEventListener("setItem", async () => {
    // 当sessionStorage 中的lang值发生变化， 给组件中的值重新赋值
    const info = decrypt((await getSession("uid")) ?? "-1")
    uid.value = info?.uid ?? -1
  });

  const minimize = () => {
    if (window.pywebview) {
      window.pywebview.api.invoke("minimize-win");
    } else {
      // 向父窗口发送消息
      window.parent.postMessage("minimize", "*");
    }
  };
  const close = () => {
    if (window.pywebview) {
      window.pywebview.api.invoke("close-win");
    } else {
      // 向父窗口发送消息
      window.parent.postMessage("close", "*");
    }
  };

  const userInfo = asyncComputed(async () => {
    if (uid.value > 0) return await api.checkUID(uid.value, relesh.value);
    else
      return {
        uid: -1,
        userName: "",
        reason: "尚未登录colg",
        show: false,
      };
  });

  return {
    uid,
    title,
    id,
    head,
    minimize,
    close,
    m_mode,
    tryChange,
    userInfo,
    relesh,
  };
});
