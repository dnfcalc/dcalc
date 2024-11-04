<script lang="ts" setup>
import { computed, onMounted, ref } from "vue"
import { debouncedWatch, useDebounceFn } from "@vueuse/core"
import api from "@/api"
import type { IRank, IRankadventure } from "@/api/info/type"
import type { TreeNode } from "@/components/calc/tree/types"

const alter = ref<string>("spitfire_female")
const pageNum = ref<number>(1)
const ranks = ref<IRank[][]>([])
const show_detail = ref<boolean[]>([])
const options = [
  ["制式武器", "CP武器"],
  ["出血", "感电", "中毒", "灼伤", "自异常", "睡眠", "低血", "半血", "无色", "基础精通", "直伤散搭"],
  ["攻速", "MP"],
  ["异常对象"],
  ["无色", "破冰"],
  ["小技能"]
]
const tags = ref<string[]>([...new Array(6).fill("")])
const rankBox = ref()



const get_ranks = () => {
  if (alter.value != "" && Number.isNaN(Number.parseInt(alter.value))) {
    api
      .rankList(
        alter.value,
        pageNum.value,
        tags.value.filter(a => a != "")
      )
      .then(r => {
        ranks.value.push(...r.data)
        show_detail.value.push(...new Array(r.data.length).fill(false))
      })
  }
}

debouncedWatch(
  tags,
  () => {
    pageNum.value = 1
    show_detail.value = []
    ranks.value = []
    get_ranks()
  },
  { deep: true, debounce: 800 }
)
const count = useDebounceFn(() => {
  // 滚动到底部，逻辑代码
  pageNum.value++
  // 记住滚动到底的时候，当前页需要加1
  get_ranks()
}, 1000)

function lazyLoading(e: any) {
  if (e.target != rankBox.value) {
    return
  }
  // // 滚动到底部，再加载的处理事件
  const scrollTop = e.target.scrollTop
  const windowHeight = e.target.clientHeight
  const scrollHeight = e.target.scrollHeight

  if (scrollTop + windowHeight >= scrollHeight - 5) {
    count()
  }
}

const advanture = ref<IRankadventure[]>([])

const items = computed<TreeNode[]>(() => {
  const nodes: TreeNode[] = []
  let index = 0
  advanture.value.forEach(a => {
    const temp: TreeNode = {
      label: a.title,
      value: index++,
      // onSelect: () => {
      //   alter.value = a.children[0].name
      // },
      children: a.children.map(b => {
        return {
          label: b.title,
          value: b.name,
          onSelect: useDebounceFn(() => {
            pageNum.value = 1
            ranks.value = []
            show_detail.value = []
            get_ranks()
          }, 800)
        }
      })
    }
    nodes.push(temp)
  })
  return nodes
})

onMounted(() => {
  rankBox.value.addEventListener("scroll", lazyLoading, true)
  api.rankAdventure().then(r => (advanture.value = r.data))
  get_ranks()
})

onMounted(() => {
  rankBox.value.removeEventListener("scroll", lazyLoading)
})
</script>

<template>
  <div class="flex flex-col items-center justify-center bg">
    <div class="h-60px w-100% mt-5px mb-5px flex flex-col items-center">
      <div class="w-80%">
        <calc-cascader v-model="alter" :items="items" class="!h-24px !w-15%" />
      </div>
      <div class="h-30px flex justify-between items-center w-80%">
        <calc-select v-for="(children, index) in options" :key="index" v-model="tags[index]" class="!w-15% !h-24px">
          <calc-option value="">
            所有
          </calc-option>
          <calc-option v-for="item in children" :key="item" :value="item">
            {{ item }}
          </calc-option>
        </calc-select>
      </div>
    </div>
    <div style="width: 100%; height: calc(100% - 60px)" :class="`ranks ${alter}`">
      <div ref="rankBox" style="height: 100%; width: 100%; overflow-y: auto; z-index: 3" class="flex flex-col items-center">
        <div class="m-10px" style="z-index: 2">
          <div v-for="(rank, index) in ranks" :key="index" class="mt-10px p-3px bg-hex-000101f2" style="border: 1px solid #483f2e">
            <div class="p-5px bg-hex-1A1A1A">
              <div class="flex">
                <div class="flex justify-center items-center w-50px pr-5px flex-col">
                  <!-- <div class="text-hex-e9c556 text-13px"> No.{{ index + 1 }} </div> -->
                  <div class="text-hex-4aa256 text-13px" @click="() => (show_detail[index] = !show_detail[index])">
                    {{ show_detail[index] ? "折叠" : "展开" }}
                  </div>
                </div>
                <div class="flex rank">
                  <div v-for="equ in rank" :key="equ.id">
                    <div
                      :class="`equipment-icon-${equ.icon
                        .split('.')[0]
                        .split('/')
                        .filter(e => !!e)
                        .join('-')}`"
                      style="border-radius: 2px; margin: 1px"
                    />
                    <div
                      v-if="equ.upgradeInfo"
                      :class="`item equipment-icon-${equ.upgradeInfo.icon
                        .split('.')[0]
                        .split('/')
                        .filter(e => !!e)
                        .join('-')}`"
                      style="border-radius: 2px; margin: 1px"
                    />
                  </div>
                </div>
              </div>
              <div v-if="show_detail[index]" class="mt-8px px-1px overflow-y-auto" style="max-height: 500px">
                <table class="w-100%" border="0" cellspacing="0" cellpadding="0">
                  <tr class="w-100%">
                    <th class="w-25% bg-hex-000000/40 h-4 !text-hex-B2966B" style="padding: 5px">
                      装备
                    </th>
                    <th class="w-75% bg-hex-000000/40 h-4 !text-hex-B2966B" style="padding: 5px">
                      详情
                    </th>
                  </tr>
                  <tr v-for="equ in rank" :key="equ.id" class="w-100%">
                    <td v-if="equ?.props" class="w-25%" align="center" style="padding: 5px">
                      <div
                        :class="`equipment-icon-${equ.icon
                          .split('.')[0]
                          .split('/')
                          .filter(e => !!e)
                          .join('-')}`"
                        style="border-radius: 2px; margin: 1px"
                      />
                      <div class="text-hex-ffb400 pt-5px">
                        {{ equ.name }}
                      </div>
                      <!-- <div
                  v-if="equ.upgradeInfo"
                  :class="`item equipment-icon-${equ.upgradeInfo.icon
                    .split('.')[0]
                    .split('/')
                    .filter(e => !!e)
                    .join('-')}`"
                  style="border-radius: 2px; margin: 1px"
                ></div
                >{{ equ.upgradeInfo?.name.replaceAll(" ", "") }} -->
                    </td>
                    <td v-if="equ?.props" class="w-75%" style="padding: 5px">
                      <div v-for="(prop, index) in equ.props" :key="index" style="padding: 2px">
                        <div class="text-hex-b59834 m-3px">
                          属性 {{ index + 1 }}
                        </div>
                        <div>
                          <div class="w-320px pl-3px text-hex-b3a987 flex-col items-center">
                            <template v-for="item in prop.split('<br/>')" :key="item">
                              <div class="mb-1px">
                                {{ item.replaceAll(" ", "") }}
                              </div>
                            </template>
                          </div>
                        </div>
                      </div>
                    </td>
                  </tr>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  // * {
  //   text-shadow: none;
  // }

  .item-head {
    background: linear-gradient(#2b2817, #171407);
    border-top: 1px solid #423d2c;
    border-bottom: 1px solid #211d15;
  }

  .bg {
    background-color: rgba(0, 1, 1, 0.95);
    overflow-y: hidden;
    height: 100%;
  }

  .rank {
    :nth-child(1),
    :nth-child(6),
    :nth-child(9) {
      margin-right: 10px;
    }
  }

  table {
    border-right: 1px solid rgba(255, 255, 255, 0.2);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  }
  td {
    border-left: 1px solid rgba(255, 255, 255, 0.2);
    border-top: 1px solid rgba(255, 255, 255, 0.2);
  }
  th {
    border-left: 1px solid rgba(255, 255, 255, 0.2);
    border-top: 1px solid rgba(255, 255, 255, 0.2);
  }

  .ranks {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: calc(100% - 60px);
    background-repeat: no-repeat;
    background-size: cover;
  }
  .ranks::after {
    content: "";
    width: 100%;
    height: calc(100% - 60px);
    position: absolute;
    top: 60px;
    left: 0;
    background-color: rgba(50, 50, 50, 0.75);
  }
</style>
