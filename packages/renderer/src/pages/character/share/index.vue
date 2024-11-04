<script lang="tsx">
import { computed, defineComponent, onMounted, ref, renderList } from "vue";
import { useRoute } from "vue-router";
import * as htmlToImage from "html-to-image";
import api from "@/api";
import type { IAnyResultInfo } from "@/api/character/type";
import { useAppStore, useBasicInfoStore, useCharacterStore, useConfigStore, useDetailsStore } from "@/store";
import { toMap } from "@/utils";
import EqIcon from "@/components/internal/equip/eq-icon.vue";
import EquipmentsVue from "@/components/internal/profile/equipments.vue";
import Watermark from "@/components/watermark/index.vue";
import CpInfo from "@/pages/character/skills/sub/cp.vue";

export default defineComponent({
  components: { EqIcon, CpInfo },
  async setup() {
    const route = useRoute();
    const uid = (route.query.res as string) ?? "";
    const characterStore = useCharacterStore();
    const configStore = useConfigStore();
    const basicStore = useBasicInfoStore();
    const detailStore = useDetailsStore();
    const imageRef = ref(null) as any;

    onMounted(() => {
      window.removeLoading();

      !basicStore.entry_list && basicStore.loadEntries();

      !basicStore.equipment_info && basicStore.loadEquips();
    });

    const result = window.pywebview
      ? await api.getResult(uid)
      : (JSON.parse(sessionStorage.getItem(uid) ?? "{}") as IAnyResultInfo);

    configStore.$patch({ token: result.token ?? configStore.token });

    const res = toMap(result, [
      "info",
      "skills",
      "skills_passive",
      "equips_forge",
      "merge_list",
      "customize",
      "specificity",
    ]) as IAnyResultInfo;
    await characterStore.load();
    // characterStore.$patch({ alter: res.alter, name: res.name })
    configStore.forge_set = res.forge_set ?? {};
    configStore.customize = res.customize ?? {};
    configStore.specificity = res.specificity ?? {};
    configStore.fusion_list = res.fusion_list ?? [];
    configStore.merge = res.merge_list;
    configStore.talisman_set = (res as any).talisman_set;
    configStore.rune_set = (res as any).rune_set;
    const part = [
      "称号",
      "宠物",
      "武器",
      "上衣",
      "下装",
      "头肩",
      "腰带",
      "鞋",
      "手镯",
      "项链",
      "戒指",
      "辅助装备",
      "魔法石",
      "耳环",
    ];

    const equips = res.equips.sort((a, b) => {
      return part.indexOf(a.part) - part.indexOf(b.part);
    });

    const fusion = ref(true);
    const fusion_armor = ref(false);
    const stable = ref(false);
    const cp = ref(true);

    const app = useAppStore();

    const showDetail=computed(()=>{
      return (app.userInfo?.show ?? false) || process.env.NODE_ENV == "development" || import.meta.env.MODE == "show"
    })

    const mergeInfo = computed(() => {
      const cur = res.equips.filter((a) => a.part == "武器")?.[0];
      return {
        weaponType: cur?.type,
        merges: configStore.merge[cur?.id ?? ""] ?? [],
      };
    });

    const specificity = computed(() => {
      const keys = Object.keys(configStore.specificity);
      if (keys.length == 0) {
        return -1;
      }
      return Math.floor(
        (Number.parseInt(Object.keys(configStore.specificity)?.[0] ?? "20000") -
          20000) /
          100
      );
    });

    const infos = computed(
      () =>
        (characterStore.especificity ?? []).find(
          (a) => a.type == specificity.value
        )?.detail ?? []
    );

    function getImage() {
      if(!showDetail.value) return
      htmlToImage
        .toCanvas(imageRef.value, {
          pixelRatio: 1.5,
        })
        .then((canvas) => {
          const imgUrl = canvas.toDataURL("image/png");
          const tempLink = document.createElement("a"); // 创建一个a标签
          tempLink.style.display = "none";
          tempLink.href = imgUrl;
          tempLink.setAttribute("download", ""); // 给a标签添加下载属性
          if (typeof tempLink.download === "undefined") {
            tempLink.setAttribute("target", "_blank");
          }
          document.body.appendChild(tempLink); // 将a标签添加到body当中
          tempLink.download = `搭配_${new Date().getTime()}`;
          tempLink.click(); // 启动下载
          document.body.removeChild(tempLink); // 下载完毕删除a标签
          window.URL.revokeObjectURL(imgUrl);
        })
        .catch((error) => {
          console.error("oops, something went wrong!", error);
        });
    }

    return () => (
      <>
        <div class="flex  text-hex-937639 items-center bg-black/70">
          {/* 说明：<textarea class="i-input !min-w-80% !h-100px" v-model={remark.value}></textarea> */}
          <div class="flex items-center justify-around ml-5px flex-1">
            <calc-checkbox v-model={fusion_armor.value}>防具贴膜</calc-checkbox>
            <calc-checkbox v-model={fusion.value}>融合石</calc-checkbox>
            <calc-checkbox v-model={stable.value}>固定装备</calc-checkbox>
            <calc-checkbox v-model={cp.value}>护石、天赋详情</calc-checkbox>
          </div>
          <calc-button disabled={!showDetail.value} class="m-5px" onClick={getImage}>
            导出图片
          </calc-button>
        </div>
        <div class="h-auto share" ref={imageRef}>
          <Watermark color="rgba(255,255,255,0.3)" fontSize={14}>
            <div class="h-300px w-100% flex flex-col items-center justify-center">
              <div class="flex items-center justify-between w-100%">
                <img
                  class="h-65px w-65px ml-10px"
                  src={`${import.meta.env.BASE_URL}favicon.ico`}
                />
                <div class="flex flex-col justify-center text-hex-ffff mr-10px">
                  <div class="text-35px font-bold italic flex justify-center">
                    {characterStore.name}
                  </div>
                  <div class="text-15px font-bold flex justify-end mr-20px">
                    {characterStore.alter
                      .split("_")
                      .map(
                        (word) => word.charAt(0).toUpperCase() + word.slice(1)
                      )
                      .join(" ")}
                  </div>
                </div>
              </div>
              <EquipmentsVue
                fusionList={configStore.fusion_list}
                equ-list={res.equips}
                showZF={false}
                showTM={true}
                tipInfo={[]}
                withBG={false}
                showTips={false}
                class="rounded-xl"
                style="border:1px solid white;background-color:rgba(0,0,0,0.7);zoom:1.15;"
                mergeInfo={mergeInfo.value}
              ></EquipmentsVue>
            </div>
            <div
              class="flex w-99% flex-wrap pl-1% py-2%"
              style="background-color:rgba(34,75,166,0.56);border-top:1px solid white"
            >
              {cp.value && (
                <div
                  class="flex items-center justify-center w-100% mr-1% my-1%"
                  style="background: linear-gradient(to right,rgba(13,17,15,0.9),rgba(35,45,54,0.7),rgba(41,53,65,0.45));border-radius:10px;border:1px solid #A6A6A6"
                >
                  <CpInfo
                    style="border-right:1px solid #A6A6A6"
                    class="w-50% flex items-center justify-center h-185px"
                    edit={false}
                  ></CpInfo>

                  {specificity.value >= 0 && (
                    <div class="flex w-50%  flex-wrap h-100% bg-hex-000/50" style="border-radius:0px 10px 10px 0px;">
                      <div style="position: relative;zoom:0.75">
                        {renderList(infos.value, (item) => {
                          return (
                            <>
                              <div
                                style={`position:absolute;left:${
                                  item.x * 60 + 10 - 8.5
                                }px;top:${item.y * 60 + 10 - 2.5}px`}
                                class="flex flex-col items-center w-66px h-66px"
                              >
                                <div
                                  class={`especificity-icon-item-${item.id}${
                                    (configStore.specificity?.[item.id] ?? 0) >
                                    0
                                      ? "_checked"
                                      : " disable"
                                  }`}
                                >
                                {(configStore.specificity?.[item.id] ?? 0) > 0 &&(<div
                                    class="flex justify-center items-center"
                                    style="position:absolute;bottom:15px;left:18px"
                                  >
                                    <div class={`lvInfo`}>
                                      <div class="w-12px h-12px ml-15px mt-2px flex items-center justify-center text-hex- text-10px">
                                        {configStore.specificity?.[item.id]}
                                      </div>
                                    </div>
                                  </div>
                                )}
                                  </div>
                              </div>
                            </>
                          );
                        })}
                      </div>
                    </div>
                  )}
                </div>
              )}
              {fusion.value && (
                <div
                  class="flex flex-wrap items-center w-100% max-h-450px mr-1% my-1% py-1%"
                  style="background: linear-gradient(to right,rgba(13,17,15,0.9),rgba(35,45,54,0.7),rgba(41,53,65,0.45));border-radius:10px;border:1px solid #A6A6A6"
                >
                  {renderList(configStore.fusion_list.map(a=>basicStore.equipment_info?.fusion?.find(
                      (b) => Number(b.id) == a
                    )).sort((a,b)=>detailStore.display_parts.findIndex(c=>c ==(a?.part ?? "")) - detailStore.display_parts.findIndex(c=>c ==(b?.part ?? ""))), (equip) => {
                    if (
                      equip &&
                      (!["头肩", "上衣", "下装", "腰带", "鞋"].includes(
                        equip.part
                      ) ||
                        fusion_armor.value)
                    ) {
                      return (
                        <>
                          <div class="flex flex-col justify-center items-center w-33%">
                            <eq-icon
                              class="mt-6px mx-10px eq-item-icon"
                              eq={equip}
                              canClick={false}
                            ></eq-icon>
                            <div class="text-hex-ffb400">{equip.name}</div>
                          </div>
                        </>
                      );
                    }
                  })}
                </div>
              )}
              {renderList(equips, (equip) => {
                if (
                  (configStore.customize?.[equip.id ?? ""] ?? []).length > 0 ||
                  (
                    (configStore.merge?.[equip.id ?? ""] ?? []).filter(
                      (a) => a > 0
                    ) ?? []
                  ).length > 0
                ) {
                  return (
                    <>
                      <div
                        class="flex items-center w-100% max-h-450px mr-1% my-1% py-1%"
                        style="background: linear-gradient(to right,rgba(13,17,15,0.9),rgba(35,45,54,0.7),rgba(41,53,65,0.45));border-radius:10px;border:1px solid #A6A6A6"
                      >
                        <div class="flex flex-col justify-center items-center w-100px">
                          <eq-icon
                            class="mt-6px mx-10px eq-item-icon"
                            eq={equip}
                            canClick={false}
                          ></eq-icon>
                          <div class="text-hex-ffb400">{equip.name}</div>
                        </div>

                        <div class="flex-1">
                          {equip.part == "武器" &&
                            (
                              (
                                configStore.merge?.[equip.id ?? ""] ?? []
                              ).filter((a) => a > 0) ?? []
                            ).length > 0 && (
                              <div>
                                <div class="text-hex-4aa256">
                                  {" "}
                                  &lt;巴卡尔融合属性&gt;{" "}
                                </div>
                                {renderList(
                                  (configStore.merge?.[equip.id ?? ""] ?? [])
                                    .filter((a) => a > 0)
                                    .sort((a, b) => a - b),
                                  (a) => {
                                    return (
                                      <div
                                        class={
                                          basicStore.entry_list?.[a.toString()]
                                            ?.type == 9
                                            ? "props-bakal"
                                            : "props-bakal-raid"
                                        }
                                      >
                                        {/* <div class="text-hex-b59834">属性 {index + 1}</div> */}
                                        {renderList(
                                          basicStore.entry_list?.[a.toString()]
                                            .props ?? [],
                                          (prop, index) => (
                                            <div class="text-12px text-hex-ffff flex mt-2px">
                                              {index == 0 ? (
                                                <div class="w-20px">{`${
                                                  (basicStore.entry_list?.[
                                                    a.toString()
                                                  ].order ?? 0) < 10
                                                    ? "0"
                                                    : ""
                                                }${
                                                  basicStore.entry_list?.[
                                                    a.toString()
                                                  ].order
                                                }.`}</div>
                                              ) : (
                                                <div class="min-w-20px">
                                                  &nbsp;
                                                </div>
                                              )}
                                              <span>{prop}</span>
                                            </div>
                                          )
                                        )}
                                      </div>
                                    );
                                  }
                                )}
                              </div>
                            )}
                          {(
                            configStore.customize?.[equip.id ?? ""] ?? []
                          ).filter((a) => a > 0).length > 0 && (
                            <div>
                              {equip.part == "武器" && (
                                <div class="text-hex-4aa256 mx-5px">
                                  {" "}
                                  &lt;定制属性&gt;{" "}
                                </div>
                              )}
                              {renderList(
                                (
                                  configStore.customize?.[equip.id ?? ""] ?? []
                                ).filter((a) => a > 0),
                                (a) => {
                                  return (
                                    <div class="props">
                                      {/* <div class="text-hex-b59834">属性 {index + 1}</div> */}
                                      <div>
                                        <>
                                          {renderList(
                                            basicStore.entry_list?.[
                                              a.toString()
                                            ].props ?? [],
                                            (prop) => (
                                              <div class="text-12px text-hex-ffff mx-5px">
                                                <span>{prop}</span>
                                              </div>
                                            )
                                          )}
                                        </>
                                      </div>
                                    </div>
                                  );
                                }
                              )}
                            </div>
                          )}
                        </div>
                      </div>
                    </>
                  );
                }
              })}

              {stable.value && (
                <div
                  class="flex flex-wrap items-center w-100% max-h-450px mr-1% my-1% py-1%"
                  style="background: linear-gradient(to right,rgba(13,17,15,0.9),rgba(35,45,54,0.7),rgba(41,53,65,0.45));border-radius:10px;border:1px solid #A6A6A6"
                >
                  {renderList(equips.sort((a,b)=>detailStore.display_parts.findIndex(c=>a.part == c)-detailStore.display_parts.findIndex(c=>b.part == c)), (equip) => {
                    if (
                      equip.alternative.length == 0 &&
                      equip.part != "称号" &&
                      equip.part != "宠物"
                    ) {
                      return (
                        <>
                          <div class="flex flex-col justify-center items-center w-33%">
                            <eq-icon
                              class="mt-6px mx-10px eq-item-icon"
                              eq={equip}
                              canClick={false}
                            ></eq-icon>
                            <div class="text-hex-ffb400">{equip.name}</div>
                          </div>
                        </>
                      );
                    }
                  })}
                </div>
              )}
            </div>
          </Watermark>
        </div>
      </>
    );
  },
});
</script>

<style lang="scss">
.disable {
  filter: grayscale(100%);
}

.lvInfo {
  background-image: url("@/assets/img/specificity/lv_active.png");
  background-repeat: no-repeat !important;
  background-size: auto auto !important;
  width: 30px;
  height: 16px;
  z-index: 10;
  color: #FEB300;
}
* {
  user-select: auto !important;
  font-family: "Microsoft Yahei" !important;
}

.share {
  background-image: url("@/assets/img/share.png");
  background-size: 100% auto;
  background-repeat: no-repeat;
  background-color: #22639e;
}

.props {
  position: relative;
  padding-left: 12px;
  line-height: 15px;

  &::before {
    content: "";
    display: inline-block;
    position: absolute;
    left: 0px;
    top: 1.5px;
    // top: 5px;
    width: 12px;
    height: 12px;
    background-image: url(@/assets/img/icon/switch.png);
  }
}

.props-bakal {
  position: relative;
  padding-left: 17px;
  line-height: 17px;

  &::before {
    content: "";
    display: inline-block;
    position: absolute;
    left: 0px;
    // top: 5px;
    width: 17px;
    height: 17px;
    background-image: url(@/assets/img/icon/bakal.png);
  }
}

.props-bakal-raid {
  position: relative;
  padding-left: 17px;
  line-height: 17px;

  &::before {
    content: "";
    display: inline-block;
    position: absolute;
    left: 0px;
    // top: 5px;
    width: 17px;
    height: 17px;
    background-image: url(@/assets/img/icon/bakalraid.png);
  }
}
</style>
