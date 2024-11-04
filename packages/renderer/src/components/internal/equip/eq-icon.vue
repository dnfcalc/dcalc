<script lang="tsx">
import { useToggle, useVModel } from "@vueuse/core"
import type { PropType } from "vue";
import { computed, defineComponent } from "vue"
import type { IEquipmentInfo } from "@/api/info/type"
import { useBasicInfoStore } from "@/store"
import { rarityClass } from "@/utils"



export default defineComponent({
  name: "EqIcon",
  props: {
    eid: {
      type: [Number, String] as PropType<ID>
    },
    eq: {
      type: Object as PropType<IEquipmentInfo>,
      default: () => null
    },
    showTips: {
      type: Boolean,
      default: false
    },
    active: {
      type: Boolean,
      default: true
    },
    hightlight: {
      type: Boolean,
      default: false
    },
    badges: {
      type: Object,
      default: () => {
        return null
      }
    },
    hightlightClass: {
      type: String,
      default: "hightLight"
    }
  },
  setup(props) {
    const active = useVModel(props, "active")
    const badgeClass = ["white", "red", "green", "blue", "yellow"]
    const toggle = useToggle(active)

    const infoStore = useBasicInfoStore()

    const equip = computed(() => {
      if (props.eq) {
        return props.eq
      }
      return infoStore.equipment_list.find(r => r.id == props.eid)
    })

    return () => {
      return (
        <div style="position:relative;z-index:5" onClick={() => toggle()}>
          <div class={props.hightlight ? props.hightlightClass : ""}></div>
          <div class={active.value ? "" : "floatLayer"}></div>
          <div class="eq-item-box">
            {equip.value && equip.value.icon ? (
              <div
                class={["eq-icon"].concat([
                  rarityClass(equip.value?.rarity ?? "")
                  // eq.value.active ? '' : 'gray'
                ])}
              >
                <div
                  class={`m-1px equipment-icon-${equip.value.icon
                    .split(".")[0]
                    .split("/")
                    .filter(e => !!e)
                    .join("-")}`}
                  style="border-radius:2px;margin:1px"
                ></div>
                <div class={`${rarityClass(equip.value?.rarity ?? "")}_effect`} style="position:absolute;top:1px;left:1px"></div>
                {true || props.badges == null ? (
                  <div></div>
                ) : props.badges.color[0] == 0 ? (
                  props.badges.num == 0 ? (
                    <div class="left kong-box">
                      <div class="kong-item"></div>
                    </div>
                  ) : (
                    <div class="left kong-box">
                      <div class={["kong-item"].concat([badgeClass[props.badges.color[0]]])}></div>
                    </div>
                  )
                ) : props.badges.num == 0 ? (
                  <div class="kong-box">
                    <div class="kong-item"></div>
                    <div class="kong-item"></div>
                  </div>
                ) : props.badges.num == 1 ? (
                  <div class="kong-box">
                    <div class={["kong-item"].concat([badgeClass[props.badges.color[0]]])}></div>
                    <div class="kong-item"></div>
                  </div>
                ) : (
                  <div class="kong-box">
                    <div class={["kong-item"].concat([badgeClass[props.badges.color[0]]])}></div>
                    <div class={["kong-item"].concat([badgeClass[props.badges.color[1]]])}></div>
                  </div>
                )}
              </div>
            ) : (
              <span class="icon"></span>
            )}
          </div>
        </div>
      )
    }
  }
})
</script>

<style scoped lang="scss">
  .eq-item-box {
    width: 30px;
    height: 30px;
    // display: inline-block;
    display: flex;
    align-content: center;
  }

  .floatLayer {
    position: absolute;
    width: 30px;
    height: 30px;
    z-index: 2;
    background-color: #00000080;
  }

  .hightLight {
    position: absolute;
    width: 30px;
    height: 30px;
    z-index: 3;
    background-image: url("@/assets/img/control/item_hover.png");
    background-size: 100% 100%;
  }

  .hightLight2 {
    position: absolute;
    width: 30px;
    height: 30px;
    z-index: 6;
    background-image: url("@/assets/img/control/item_checked.png");
    background-size: 100% 100%;
  }
  .eq-icon {
    // image-rendering:pixelated;
    width: 30px;
    height: 30px;
    position: relative;
    display: inline-block;
    border-radius: 2px;
    overflow: hidden;

    &.gray {
      -webkit-filter: grayscale(100%);
      -moz-filter: grayscale(100%);
      -ms-filter: grayscale(100%);
      -o-filter: grayscale(100%);
      filter: grayscale(100%);
      filter: gray;
    }

    &::before {
      content: "";
      width: 26px;
      height: 26px;
      position: absolute;
      // border: 1px solid rgba(#666666, 0.5);
      top: 1px;
      left: 1px;
      z-index: 1;
    }

    &::after {
      content: "";
      width: 30px;
      height: 30px;
      position: absolute;
      top: 0;
      left: 0;
      background-image: url(@/assets/img/rarity/稀有.png);
      background-size: 100%;
      //border: 1.5px solid;
      //border-image: linear-gradient(#e7a300, #000) 1;
      //clip-path: inset(0 round 2px);
    }

    &.normal {
      &::after {
        background-image: url(@/assets/img/rarity/史诗.png);
      }
    }
    &.advanced {
      &::after {
        border-image: linear-gradient(#61c8de, #000) 1;
      }
    }
    &.rare {
      &::after {
        background-image: url(@/assets/img/rarity/稀有.png);
      }
    }
    &.artifact {
      &::after {
        background-image: url(@/assets/img/rarity/神器.png);
      }
    }
    &.legend {
      &::after {
        background-image: url(@/assets/img/rarity/传说.png);
      }
    }
    &.epic {
      &::after {
        background-image: url(@/assets/img/rarity/史诗.png);
      }
    }
    &.myth {
      &::after {
        background-image: url(@/assets/img/rarity/神话.png);
      }
    }
    &.primeval {
      &::after {
        background-image: url(@/assets/img/rarity/太初.png);
      }
    }
    // &.can-click:hover {
    //   cursor: pointer;
    //   background-image: linear-gradient(#3ae7fa, #3ae7fa);
    // }

    // > img {
    //   position: relative;
    //   top: 0;
    //   left: 0;
    //   width: 30px;
    //   height: 30px;
    //   border-radius: 2px;
    // }

    .kong-box {
      width: 14px;
      height: 7px;
      position: absolute;
      bottom: 1px;
      right: -1px;
      display: flex;

      &.left {
        right: auto;
        left: 0;
        width: 7px;
      }

      .kong-item {
        width: 7px;
        position: relative;
        border: 1px solid #637b39;
        background-color: #522910;
        &::after {
          content: "";
          display: block;
          height: 3px;
          border: 1px solid rgba(#000, 0.5);
        }

        &:last-child {
          right: 1px;
        }

        &.red {
          background: linear-gradient(to left top, #ff108c, #ff73c6, #ad0852, #ff108c, #ffffff, #ffffff);
        }
        &.blue {
          background: linear-gradient(to left top, #10ceff, #73e7ff, #086bad, #10ceff, #ffffff, #ffffff);
        }
        &.green {
          background: linear-gradient(to left top, #b5ff10, #efff73, #63ad08, #b5ff10, #ffffff, #ffffff);
        }
        &.yellow {
          background: linear-gradient(to left top, #ffbd10, #ffd673, #ad6308, #ffbd10, #ffffff, #ffffff);
        }
        &.white {
          border: 1px solid #ffde5a;
          background: linear-gradient(to left top, #efffff, #ceffff, #4a7bde, #efffff, #efffff, #ffffff);
        }
      }
    }
  }
</style>
