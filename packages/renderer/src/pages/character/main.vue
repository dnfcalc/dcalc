<script lang="tsx">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import { computed, defineComponent, h, onBeforeUnmount, onMounted, ref, renderList } from "vue"
import { useRoute } from "vue-router"
import Update from "../update.vue"
import ShareVue from "./config/share.vue"
import ImportVue from "./config/import.vue"
import { useDialog } from "@/components/hooks/dialog"
import { useOpenWindow } from "@/hooks/open"
import { useAppStore, useBasicInfoStore, useCharacterStore, useConfigStore, useDetailsStore, useGlobalStore } from "@/store"
import type { IMonster } from "@/api/info/type"
import { decrypt, getSession, toObj } from "@/utils"

// import Character from "@/pages/character/character/character.vue"
// import Customize from "@/pages/character/customize/customize.vue"
// import Equipment from "@/pages/character/equipment/equipment.vue"
// import Detail from "@/pages/character/detail/detail.vue"
// import Singleset from "@/pages/character/singleset/singleset.vue"

export default defineComponent(() => {
  const route = useRoute()
  const { alert, confirm } = useDialog()
  const openUrl = useOpenWindow()
  const char = route.query.alter as string
  const version = route.query.version as string
  const r = route.query.r as string
  const globalStore = useGlobalStore()
  const configStore = useConfigStore()
  const characterStore = useCharacterStore()
  const basicStore = useBasicInfoStore()
  const canClick = ref(true)
  const checkUpdate = ref<boolean>(false)
  const app = useAppStore()

  onMounted(async () => {
    window.removeLoading()
    window.addEventListener("unload", save_config)
    if (window.pywebview) {
      app.relesh = new Date().getTime();
    }
    useAppStore().uid = decrypt(await getSession("uid"))?.uid ?? -1
  })

  onBeforeUnmount(() => {
    window.removeEventListener("unload", save_config)
  })

  function save_config() {
    configStore.save()
  }

  const shareVisible = ref(false)
  async function showShare() {
    configStore.save()
    shareVisible.value = true
  }

  const importVisible = ref(false)
  async function showImport() {
    importVisible.value = true
  }

  const detailsStore = useDetailsStore()

  const title = computed(() => {
    return app.uid > 0 ? `当前用户：${app.userInfo.uid}(${app.uid}) 请勿用于打桩排名等节奏` : "请勿用于打桩排名等节奏"
  })

  async function calc() {
    canClick.value = false
    // alert({
    //   content: () => <>暂不支持多套计算</>
    // })
    // return
    // 一堆前处理和判断，然后计算
    if (!(route.path.endsWith("/singleset") || route.path.endsWith("/comparison"))) {
      if (configStore.skill_que.length == 0 && characterStore.is_delear) {
        await alert({
          content: "请先设置技能次数"
        })
        canClick.value = true
        return
      }
      const total = ((configStore as any).equ_sort as number[][]).reduce((a, b) => a * b.length, 1)
      if (total == 0) {
        await alert({
          content: "请确保每个部位都选择了装备"
        })
        canClick.value = true
        return
      }
      let max = 500
      if (window.pywebview) {
        max = 1000000
      }
      if (total > max) {
        await alert({
          content: `${max},请酌情减少各部位数量后再计算`
        })
        canClick.value = true
        return
      }

      const res = await confirm({
        content: () => {
          if (window.pywebview) {
            return h(
              "div",
              { class: "justify-center text-center", style: "white-space:pre-wrap;width:250px;color:white" },
              `共计${total.toLocaleString()}个组合\n\n多套计算为实验性功能,后续会进行减枝优化\n请酌情减少各部位数量,尤其称号 武器 宠物\n\n组合较多时,CPU和内存会拉满且耗时较久\n\n大批次数据炸机自行承担,是否确认计算??!!`
            )
          } else {
            return h(
              "div",
              { class: "justify-center text-center", style: "white-space:pre-wrap;width:250px;color:white" },
              `共计${total.toLocaleString()}个组合\n\n服务器不支持超过500个组合\n请酌情减少各部位数量,尤其称号 武器 宠物\n\n是否确认计算??!!`
            )
          }
        }
      })
      if (res.isOk) {
        const saveData = await configStore.calc(route.path.endsWith("/singleset") || route.path.endsWith("/comparison"))
        canClick.value = true
        if (saveData && saveData?.id) {
          // 排行界面
          if (window.pywebview) {
            openUrl(`/ranking?res=${saveData.id}`, { width: 700, height: 650 })
          } else {
            saveData.forge_set = toObj(configStore).forge_set
            saveData.merge_list = configStore.merge
            saveData.fusion_list = configStore.fusion_list as number[]
            saveData.customize = configStore.customize
            saveData.specificity = configStore.specificity
            ;(saveData as any).talisman_set = configStore.talisman_set ?? []
            ;(saveData as any).rune_set = configStore.rune_set ?? []
            saveData.equips = basicStore.equipment_list.filter(a => configStore.single_set.includes(a.id)) ?? []
            sessionStorage.setItem(saveData.id.toString() ?? "", JSON.stringify(saveData))
            openUrl(`/ranking?res=${saveData.id}`, { target: "_blank" })
          }
        }
      }
    } else {
      const saveData = await configStore.calc(route.path.endsWith("/singleset") || route.path.endsWith("/comparison"))
      canClick.value = true
      saveData.forge_set = toObj(configStore).forge_set
      saveData.merge_list = configStore.merge
      saveData.fusion_list = configStore.fusion_list as number[]
      saveData.customize = configStore.customize
      saveData.specificity = configStore.specificity
      ;(saveData as any).talisman_set = configStore.talisman_set ?? []
      ;(saveData as any).rune_set = configStore.rune_set ?? []
      saveData.equips = basicStore.equipment_list.filter(a => configStore.single_set.includes(a.id)) ?? []
      // 详情界面
      if (saveData && saveData?.id) {
        if (!window.pywebview) {
          sessionStorage.setItem(saveData.id?.toString() ?? "", JSON.stringify(saveData))
        }
        openUrl(`/result?res=${saveData.id}`, { query: { res: `${saveData.id}`, standard: `${detailsStore.standard_uuid}` }, width: 890, height: 635, title: title.value })
      }
    }
    canClick.value = true
  }

  function update() {
    checkUpdate.value = false
    setTimeout(() => {
      checkUpdate.value = true
    }, 500)
  }

  const openSet = async () => {
    const res = await openUrl("/set", { width: 600, height: 500 })
    if (res) {
      characterStore.reload()
    }
  }

  return () => {
    !characterStore.alter && globalStore.isReady && characterStore.newCharacter(char, version, globalStore.global_set_details?.[1].toString())
    if (characterStore.alter) {
      return (
      // style={`background-image:url(/images/characters/${characterStore.alter}.jpg)`}
        <div class={`main ${characterStore.alter}`}>
          {checkUpdate.value && <Update />}
          {
            // <WatermarkVue content="test" class="h-full w-full top-0 left-0 absolute" src={`/images/characters/${characterStore.alter}/bg.jpg`} />
            // <div class="header">
          }
          <div class="header">
            <calc-tabs route query={{ alter: char, version, r }}>
              <calc-tab value={"/character/singleset"}>单套选择</calc-tab>
              <calc-tab value={"/character/skills"}>技能设置</calc-tab>
              <calc-tab value={"/character/profile"}>打造设置</calc-tab>
              {/* <calc-tab value={"/character/equips"}>多套计算</calc-tab> */}
              <calc-tab value={"/character/customize"}>定制史诗词条</calc-tab>
              <calc-tab value={"/character/specificity"}>装备特性</calc-tab>
              <calc-tab value={"/character/merge"}>装备融合</calc-tab>
              <calc-tab value={"/character/comparison"}>定制史诗分析</calc-tab>
            </calc-tabs>
          </div>
          <div class="center">
            {characterStore.alter && (
              <router-view>
                {
                  //   ({ Component }: { Component: any }) => {
                  //   return (
                  //     <KeepAlive>
                  //       <Component is={false} />
                  //     </KeepAlive>
                  //   )
                  // }
                }
              </router-view>
            )}
          </div>

          <div class="footer">
            <div class="flex col-4 justify-start items-center">
              <calc-button onClick={() => openUrl("https://dnftools.com/", { width: 0, height: 0, target: "_blank" })} title="主页" class="ml-1" icon="home"></calc-button>
              {window.pywebview && <calc-button onClick={update} title="检查更新" class="ml-1" icon="update"></calc-button>}
              <calc-button onClick={characterStore.reload} title="刷新" class="ml-1" icon="reflesh"></calc-button>
              <calc-button onClick={openSet} title="设置" class="ml-1" icon="set"></calc-button>
              <calc-button title="存档分享" onClick={showShare} class="ml-1" icon="share"></calc-button>
              <calc-button title="存档导入" onClick={showImport} class="ml-1" icon="import"></calc-button>
            </div>
            <div class="flex col-4 justify-center"></div>
            <div class="flex col-4 justify-center">
              <calc-select onChange={() => (route.path.endsWith("/singleset") || route.path.endsWith("/comparison")) && characterStore.calc()} v-model={configStore.carry_type} class="!h-22px">
                {renderList(characterStore.carry_type_list, item => (
                  <calc-option value={item}>{item}</calc-option>
                ))}
              </calc-select>
            </div>
            <div class="flex col-4 justify-center">
              <calc-select onChange={() => (route.path.endsWith("/singleset") || route.path.endsWith("/comparison")) && characterStore.calc()} v-model={configStore.scene} class="!h-22px">
                {renderList(basicStore.scenes_list as IMonster[], item => (
                  <calc-option value={item.id}>{item.name}</calc-option>
                ))}
              </calc-select>
            </div>
            <div class="flex col-4 justify-center">
              <calc-select onChange={() => (route.path.endsWith("/singleset") || route.path.endsWith("/comparison")) && characterStore.calc()} v-model={configStore.monster} class="!h-22px">
                {renderList(basicStore.monster_list as IMonster[], item => (
                  <calc-option value={item.id}>{item.name}</calc-option>
                ))}
              </calc-select>
            </div>
            <div class="flex col-4 justify-center">
              <calc-button class="w-80% !h-28px" disabled={!canClick.value} onClick={calc}>
                  开始计算
              </calc-button>
            </div>
            <calc-dialog lazy header="存档分享" v-model:visible={shareVisible.value}>
              <ShareVue></ShareVue>
            </calc-dialog>
            <calc-dialog lazy header="存档导入" v-model:visible={importVisible.value}>
              <ImportVue></ImportVue>
            </calc-dialog>
          </div>
        </div>
      )
    }
    return <div></div>
  }
})
</script>

<style lang="scss">
  .main {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
    background-repeat: no-repeat;
    background-size: cover;
    background-color: black;

    color: #e9c558;
    // font-size: 12px;

    .header {
      display: flex;
      align-items: flex-end;
      z-index: 2;
      height: 26px;
    }

    .footer {
      display: flex;
      align-items: center;
      justify-content: end;
      z-index: 2;
      height: 40px;
    }

    .center {
      flex: 1;
      overflow-y: auto;
      overflow-x: hidden;
      z-index: 2;
      width: 100%;
    }
  }

  .main::after {
    content: "";
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    background-color: rgba(50, 50, 50, 0.75);
  }
</style>
