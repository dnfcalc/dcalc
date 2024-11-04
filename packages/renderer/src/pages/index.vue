<script lang="tsx">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import type { CSSProperties } from "vue";
import { Suspense, computed, defineComponent, onMounted, ref, watch } from "vue"
import { RouterView, useRoute } from "vue-router"
import { useDialog } from "@/components/hooks/dialog"
import { useAppStore } from "@/store/app"
import { useConfigStore, useGlobalStore } from "@/store";
import { decrypt, getSession } from "@/utils";

export default defineComponent({
  setup() {
    const appStore = useAppStore()
    const globalStore = useGlobalStore()

    const { render } = useDialog()

    const title = computed(() => {
      const route = useRoute()
      return route.meta.title ?? appStore.title
    })

    let initialX = 0;
    let initialY = 0;

    function onMouseMove(ev: any) {
      const x = ev.screenX - initialX;
      const y = ev.screenY - initialY;
      window.pywebview._bridge.call("moveWindow", [x, y], "move");
    }

    const titleRef = ref()

    function onMouseUp() {
      window.removeEventListener("mousemove", onMouseMove);
      window.removeEventListener("mouseup", onMouseUp);
    }

    function onMouseDown(ev: any) {
      initialX = ev.clientX;
      initialY = ev.clientY;
      window.addEventListener("mouseup", onMouseUp);
      window.addEventListener("mousemove", onMouseMove);
    }

    onMounted(() => {
      if (window.pywebview) {
        titleRef.value.addEventListener("mousedown", onMouseDown);
      }
    })

    watch(() => globalStore.global_set_details[4], () => {
      document.body.style.fontFamily = `dcalc,${globalStore.global_set_details[4] == 0 ? "SimSun" : "SimHei"}`
    })


    const style = computed<CSSProperties>(() => {
      if (!window.pywebview) {
        return {
          textRendering: "geometricPrecision",
          letterSpacing: "-0.1px",
          fontFamily: `dcalc,${globalStore.global_set_details[4] == 0 ? "SimSun" : "SimHei"}`
        }
      } else {
        return {
          fontFamily: `dcalc,${globalStore.global_set_details[4] == 0 ? "SimSun" : "SimHei"}`
        }
      }
    })

    onMounted(async ()=>{
      useAppStore().uid = decrypt(await getSession("uid"))?.uid ?? -1
    })

    // watch(()=>
    //   (useConfigStore()).uid,
    //   (val)=>{
    //     appStore.checkUID(val ?? -1)
    //   }
    // )

    return () => (
      <>
        <div style={style.value} class="w-full h-full">
          <div ref={titleRef}
            class="bg-hex bg-gradient-to-t flex from-hex-273e69 to-hex-335793 h-6 px-2 top-0 right-0 left-0 leading-6  z-999 app-header layout-title items-center justify-between fixed"
            style={`-webkit-app-region: drag;${window.pywebview ? "" : "display:none"}`}
          >
            <div class="h-4 leading-4 w-4" style="background-image:url('./favicon.ico');background-size: 100% 100%;"></div>
            <div class="text-xs text-shadow header">
              {title.value} {`(${APP_VERSION})`}
            </div>
            <div class="flex items-center">
              <div onClick={appStore.minimize} class="cursor-pointer min-icon h-4  text-center mr-4 text-hex-f0d070 text-opacity-72 w-4 hover:text-opacity-100"></div>
              <div onClick={appStore.close} class="cursor-pointer h-4 text-center  text-hex-f0d070 text-opacity-72  w-4 close-icon hover:text-opacity-100"></div>
            </div>
          </div>

          <div class={["w-full overflow-y-auto"].concat(window.pywebview ? "mt-6" : "mt-0")} style={window.pywebview ? "height:calc(100% - 24px);" : "height:100%"}>
            <Suspense>
              <RouterView></RouterView>
            </Suspense>
          </div>
          {render()}
        </div>
      </>
    )
  }
})
</script>

<style scoped>
  .app {
    height: 100%;
  }
</style>
