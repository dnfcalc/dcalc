<script lang="tsx">
import { computed, defineComponent, onMounted, ref, renderList } from "vue";
import { useCharacterStore, useConfigStore } from "@/store";
import { formatStr } from "@/utils";
import type { ISItemInfo } from "@/api/info/type";



export default defineComponent({
  props: {
    simple: {
      type: Boolean,
      default: false
    }
  },
  setup(props) {
    const characterStore = useCharacterStore()

    enum STATUS {
      "不可学习" = 0,
      "可学习" = 1,
      "已学习" = 2,
      "激活焦点" = 3,
      "不可增加等级" = 4,
      "不可减少等级" = 5
    }

    const cost = ref(0)
    const max = 1300
    // const remaind = computed(() => max - cost.value)
    const configStore = useConfigStore()
    const tab = ref(3)
    const infos = computed(() => (characterStore.especificity ?? []).find(a => a.type == tab.value)?.detail ?? [])
    const cur = ref(-1)
    const x = computed(() => props.simple ? 80 : 100)
    const y = computed(() => props.simple ? 120 : 140)

    const renderLine = (item: any, status: STATUS) => {
      const preInfo = item.preconditions?.[0]
      const pre = infos.value.find((a) => a.id == preInfo.id);
      if (pre) {
        const pre_y = pre.x * x.value + 10;
        const pre_x = pre.y * y.value + 10;
        const item_y = item.x * x.value + 10;
        const item_x = item.y * y.value + 10;
        if (item_y < pre_y) {
          return (<>
            <div class={`treeLine${status > 0 ? "Active" : ""}`} style={`left:${pre_y + 25 - 2}px;top:${pre_x + 50}px;height:${(item_x - pre_x - 50) / 2}px;z-index:${10 - preInfo.needLv}`}></div>
            <div class={`treeLine${status > 0 ? "Active" : ""}`} style={`left:${item_y + 25 - 2}px;top:${item_x - (item_x - pre_x - 50) / 2}px;width:${pre_y - item_y + 4}px;z-index:${10 - preInfo.needLv}`}></div>
            <div class={`treeLineWithArrow${status > 0 ? "Active" : ""}`} style={`left:${item_y + 25 - 2}px;top:${item_x - (item_x - pre_x - 50) / 2}px;height:${(item_x - pre_x - 50) / 2 - 2}px;z-index:${10 - preInfo.needLv}`}></div>
          </>)
        }
        if (item_y == pre_y) {
          return (<>
            <div class={`treeLineWithArrow${status > 0 ? "Active" : ""}`} style={`left:${item_y + 25 - 2}px;top:${pre_x + 50}px;height:${item_x - pre_x - 50 - 2}px;z-index:${10 - preInfo.needLv}`}></div>
          </>)
        }
        if (item_y > pre_y) {
          return (<>
            <div class={`treeLine${status > 0 ? "Active" : ""}`} style={`left:${pre_y + 25 - 2}px;top:${pre_x + 50}px;height:${(item_x - pre_x - 50) / 2}px;z-index:${10 - preInfo.needLv}`}></div>
            <div class={`treeLine${status > 0 ? "Active" : ""}`} style={`left:${pre_y + 25 - 2}px;top:${item_x - (item_x - pre_x - 50) / 2}px;width:${-pre_y + item_y + 4}px;z-index:${10 - preInfo.needLv}`}></div>
            <div class={`treeLineWithArrow${status > 0 ? "Active" : ""}`} style={`left:${item_y + 25 - 2}px;top:${item_x - (item_x - pre_x - 50) / 2}px;height:${(item_x - pre_x - 50) / 2 - 2}px;z-index:${10 - preInfo.needLv}`}></div>
          </>)
        }
      } else {
        return (
          <>
          </>
        )
      }
    }

    // 是否可以减少等级，主要判断是否已经有点过的前置技能

    const canReduce = (item: ISItemInfo) => {
      const lv = configStore.specificity[item.id.toString()] ?? 0
      if (lv - 1 < 0) {
        return false
      }

      const flag = !Object.keys(configStore.specificity).some(key => {
        if (key.toString() != item.id.toString()
        && (configStore.specificity[key] ?? 0) > 0
        && ((((infos.value.find(a => a.id.toString() == key)?.preconditions ?? []).find(a => a.id == item.id)?.needLv ?? 0) > lv - 1)
          || (configStore.specificity[key] > 1
          && ((((infos.value.find(a => a.id.toString() == key)?.lvinfo ?? [])?.[configStore.specificity[key] - 1].needprecost) + ((infos.value.find(a => a.id.toString() == key)?.lvinfo ?? [])?.[configStore.specificity[key] - 2].cost)) > (cost.value - (item.lvinfo.find(a => a.lv == lv)?.cost ?? 0))))
        )) {
          return true
        }
        return false
      })
      return flag
    }

    const reduce = (item: ISItemInfo) => {
      return (event?: any) => {
        event?.stopPropagation()

        let count = 1
        if (event?.ctrlKey) {
          count = (configStore.specificity[item.id.toString()] ?? 0)
        }

        for (let i = 0; i < count; i++) {
          if (!canReduce(item)) {
            return
          }
          const lv = configStore.specificity[item.id.toString()] ?? 0
          const curLv = item.lvinfo.find(a => a.lv == lv)
          if (curLv) {
            cost.value -= curLv.cost
          }
          configStore.specificity[item.id.toString()] = lv - 1
        }
      }
    }

    // 是否可以增加等级

    const canInrease = (item: ISItemInfo) => {
      const lv = configStore.specificity[item.id.toString()] ?? 0
      if (lv >= item.master
      || (item.masterWith ?? []).reduce((a, b) => a + (configStore.specificity[b.toString()] ?? 0), 0) + lv >= (item.masterWithMax ?? item.master)
      || item.lvinfo[lv].needprecost > cost.value
      ) {
        return false
      }

      const nextLv = item.lvinfo.find(a => a.lv == lv + 1)
      if (!nextLv || (nextLv && cost.value + nextLv.cost > max)) {
        return false
      }

      return true
    }

    const increase = (item: ISItemInfo) => {
      return (event: any) => {
        event?.stopPropagation()

        let count = 1
        if (event?.ctrlKey) {
          count = item.master - (configStore.specificity[item.id.toString()] ?? 0)
        }


        for (let i = 0; i < count; i++) {
          const lv = configStore.specificity[item.id.toString()] ?? 0
          const nextLv = item.lvinfo.find(a => a.lv == lv + 1)
          if (!canInrease(item)) {
            return
          }
          if (nextLv) {
            cost.value += nextLv.cost
          }
          configStore.specificity[item.id.toString()] = (configStore.specificity[item.id.toString()] ?? 0) + 1
        }
      }
    }

    const active = (item: ISItemInfo, status: number) => {
      return (event: any) => {
        if (status < STATUS.可学习) {
          return
        }
        if (cur.value == item.id || event.ctrlKey) {
          increase(item)(event)
        } else {
          cur.value = item.id
        }
      }
    }

    const rightActive = (item: ISItemInfo, status: number) => {
      return (event: any) => {
        if (status < STATUS.可学习) {
          return
        }
        event.preventDefault()
        if (cur.value == item.id || event.ctrlKey) {
          reduce(item)(event)
        }
      }
    }

    const changeTab = (index: number) => {
      if (tab.value == index) {
        return
      }
      tab.value = index
      configStore.specificity = {}
      cost.value = 0
      cur.value = -1
    }


    onMounted(() => {
      if (!configStore.specificity) {
        configStore.specificity = {}
      }
      tab.value = Math.floor(((Number.parseInt(Object.keys(configStore.specificity)?.[0] ?? "20000") - 20000) / 100))
      cost.value = Object.keys(configStore.specificity).reduce((pre, cur) => {
        return pre + (infos.value.find(a => a.id.toString() == cur)?.lvinfo.filter(a => a.lv <= configStore.specificity[cur]) ?? []).reduce((pre_a, cur_a) => cur_a.cost + pre_a, 0)
      }, 0)
    });
    return () => {
      return (
        <>
          <div class="bg-hex-111111 w-100% h-100% flex flex-col" style={`width:${props.simple ? "645px" : "1100px"}`}>
            <div class={`h-83px w-100% head_${tab.value} flex items-center justify-around`}>
              {renderList(4, index => (<div class={"w-25% h-100% flex items-center justify-center"}>
                <div onClick={() => changeTab(index - 1)} style="zoom:0.8" class={`especificity-icon-title-${index - 1} ${index - 1 == tab.value ? "" : "disable"}`}></div>
              </div>))}
            </div>
            <div class="flex w-100%  flex-1">
              <div class="w-50% h-auto p-5px">
                <div class="h-20px w-full bg-hex-000000 flex items-center justify-center" style="border:2px solid #23180A">
                  <div class="text-hex-8C7B5E">特性点数</div>
                  <div class="specificitySystem mx-5px"></div>
                  <div class="text-hex-3ea74e">{cost.value} / {max} </div>
                </div>
                <div class="h-430px w-430px" style="position:relative">
                  {renderList(infos.value, (item) => {
                    let status: STATUS
                    const lv = configStore.specificity?.[item.id] ?? 0

                    if (item.preconditions.reduce((pre, cur) => pre && ((configStore.specificity?.[cur.id] ?? 0) >= cur.needLv), true) && (item.lvinfo[0].needprecost <= cost.value)) {
                      status = lv > 0 ? STATUS.已学习 : STATUS.可学习;
                      // 激活
                      if (cur.value == item.id) {
                        status = STATUS.激活焦点
                      }
                    } else {
                      status = STATUS.不可学习
                    }

                    (item.conflict ?? []).forEach(a => {
                      if ((configStore.specificity?.[a] ?? 0) > 0) {
                        status = STATUS.不可学习
                      }
                    })



                    return (
                      <>
                        <div style={`position:absolute;left:${item.x * x.value + 10 - 8.5}px;top:${item.y * y.value + 10 - 2.5}px`} class="flex flex-col items-center w-66px h-66px" onClick={ active(item, status) } onContextmenu ={rightActive(item, status)}>
                          <div class={`especificity-icon-item-${item.id}${lv > 0 ? "_checked" : ""} ${status == 0 ? "disable" : ""}`}>
                            {status == STATUS.激活焦点 && <div class="specificity_check"></div>}
                          </div>
                          <div class="flex justify-center items-center" style="position:relative;bottom:10px">
                            {status == STATUS.激活焦点 && <calc-button disabled={!canReduce(item)} onClick={reduce(item)} icon="reduce"></calc-button>}
                            {status > STATUS.不可学习 && (<div class={`lvInfo${lv == item.master ? "Master" : (lv > 0 || status == STATUS.激活焦点 ? "Active" : "")}`}>
                              <div class="w-12px h-14px ml-15px mt-2px flex items-center justify-center text-hex- text-10px">
                                {status > 0 && lv}
                              </div>
                            </div>)}
                            {status == STATUS.激活焦点 && <calc-button disabled={!canInrease(item)} onClick={increase(item)} icon="increase"></calc-button>}
                          </div>
                        </div>
                        {item.preconditions.length > 0 && item.preconditions.length > 0 && renderLine(item, status)}
                      </>
                    )
                  }
                  )}
                </div>
              </div>
              <div class="flex-1" style={`border-left: 2px solid rgba(255, 255, 255, 0.1);${props.simple ? "height:440px;overflow-y:auto;padding-top:10px;padding-bottom:10px" : ""}`}>
                {renderList(Object.keys(configStore.specificity ?? {}), key => {
                  const lv = configStore.specificity[key]
                  const info = infos.value.find(a => a.id.toString() == key)
                  if (lv > 0 && info) {
                    const nums = info.lvinfo[lv - 1].params.map(a => `<span style='color:#D6C591'>${a}</span>`)
                    return (<>
                      <div class="desItem">
                        <div class="text-hex-C1A336">{info.name}</div>
                        <div class="text-hex-A1854A">{
                          renderList(formatStr(info.desc, nums).split("<br/>"), item => (<div v-html={item}></div>))}


                        {(info.lvinfo[lv - 1]?.remark?.length ?? 0) > 0 && <div class="text-hex-6A5E3A mt-1px">
                          {renderList(info.lvinfo[lv - 1].remark, item => {
                            const remarks = item.split("<br/>")
                            return (<>
                              {renderList(remarks, remark => (<div>
                                {remark}
                              </div>))}
                            </>)
                          })}</div>}
                        </div>
                      </div>
                    </>)
                  }
                })}

              </div>
            </div>
          </div>
        </>
      );
    };
  }
});
</script>

<style lang="scss">
.desItem{

  padding: 5px;

  &:not(:first){
    margin-top: 10px;
  }
}

.head_0{
  background-image: url("@/assets/img/specificity/0.png");
  background-repeat: no-repeat !important;
  background-size: 100% 100% !important;
}

.head_1{
  background-image: url("@/assets/img/specificity/1.png");
  background-repeat: no-repeat !important;
  background-size: 100% 100% !important;
}

.head_2{
  background-image: url("@/assets/img/specificity/2.png");
  background-repeat: no-repeat !important;
  background-size: 100% 100% !important;
}

.head_3{
  background-image: url("@/assets/img/specificity/3.png");
  background-repeat: no-repeat !important;
  background-size: 100% 100% !important;
}

.specificitySystem{
  height: 15px;
  width: 15px;
  background-image: url("@/assets/img/specificity/system.png");
  background-repeat: no-repeat !important;
  background-size: 100% 100% !important;
}

.treeLine {
  position: absolute;
  height: 4px;
  width: 4px;
  background: #414141;
}

.treeLineWithArrow {
  position: absolute;
  height: 4px;
  width: 4px;
  background: #414141;
  &::after {
    content: "";
    width: 0;
    height: 0;
    border-top: 6px solid #414141;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    position: absolute;
    bottom: -2px;
    left: -4px;
  }
}

.treeLineActive {
  position: absolute;
  height: 4px;
  width: 4px;
  background: #5B3E2D;
}

.treeLineWithArrowActive {
  position: absolute;
  height: 4px;
  width: 4px;
  background: #5B3E2D;
  &::after {
    content: "";
    width: 0;
    height: 0;
    border-top: 6px solid #5B3E2D;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    position: absolute;
    bottom: -2px;
    left: -4px;
  }
}

.disable{
  filter: grayscale(100%);
}


.specificity_check{
  background-image: url("@/assets/img/specificity/select.png");
  z-index: 10;
  width: 49px;
  height: 49px;
}
</style>
