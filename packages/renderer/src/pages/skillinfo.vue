<script lang="ts" setup>
import { computed, onMounted, ref } from "vue"
import { useDebounceFn } from "@vueuse/core"
import api from "@/api"
import type { IAdventureInfo, ISkillInfo } from "@/api/info/type"
import type { TreeNode } from "@/components/calc/tree/types"

const alter = ref<string>("weapon_master")

const name = ref<string>("极诣·剑魂")
const weapon = ref<string>("")
const skillInfos = ref<ISkillInfo[]>([])

const alter_abbr = computed(() => {
  try {
    return alter.value?.split(".")?.splice(-1)?.[0]
  } catch (e) {
    return ""
  }
})

const weapons = computed(() => skillInfos.value?.map(a => a.weapon))


const get_skills = () => {
  if (alter.value != "" && Number.isNaN(Number.parseInt(alter.value)) && alter_abbr.value != "") {
    api.skillInfoList(alter.value).then(r => {
      skillInfos.value = r
      weapon.value = weapons.value[0]
    })
  }
}

const cur_weapon_skill = computed(() => {
  const temp = skillInfos.value?.find(a => a.weapon == weapon.value)
  if (temp) {
    temp.skills_active = temp.skills_active
    // .filter(a => a.data > 0)
      .sort((a, b) => {
        return b.need_level + ([50, 85, 100].indexOf(b.need_level) + 1) * 100 + (b.cost ?? 0) - (a.need_level + ([50, 85, 100].indexOf(a.need_level) + 1) * 100 + (a.cost ?? 0))
      })
  }
  return temp
})


const max_cols = computed(() =>
  Math.max((cur_weapon_skill.value?.skills_active.length ?? 0) + 1, (cur_weapon_skill.value?.skills_cp.length ?? 0) + 3 + (cur_weapon_skill.value?.skills_passive.length ?? 0))
)


const advanture = ref<IAdventureInfo[]>([])

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
      children: a.children
        .filter(c => c.name != "empty" && c.title != "")
        .map(b => {
          if ((b.options ?? []).length > 0) {
            return {
              label: b.title,
              value: index++,
              children: b.options?.map(c => {
                return {
                  label: `${b.title}-${c.title}`,
                  value: c.class ?? a.name,
                  onSelect: useDebounceFn(() => {
                    name.value = `${b.title}-${c.title}`
                    get_skills()
                  }, 800)
                }
              })
            }
          } else {
            return {
              label: b.title,
              value: b.name,
              onSelect: useDebounceFn(() => {
                name.value = b.title
                get_skills()
              }, 800)
            }
          }
        })
    }
    nodes.push(temp)
  })
  return nodes
})

onMounted(() => {
  api.adventures().then(r => (advanture.value = r.data))
  get_skills()
})
</script>

<template>
  <div class="skillinfo flex flex-col items-center justify-center h-auto min-h-full w-100% bg-cover bg-hex-EFEFEF">
    <div class="h-70px w-100% mt-35px mb-5px flex flex-col items-center flex">
      <calc-cascader v-model="alter" :items="items" class="!h-24px !w-200px" />
      <calc-select v-model="weapon" class="!h-24px !w-200px !my-10px">
        <calc-option v-for="item in weapons" :key="item" :value="item">
          {{ item }}
        </calc-option>
      </calc-select>
    </div>
    <!-- <div style="width: 100%; height: calc(100% - 34px)" :class="'ranks ' + alter"> -->
    <div style="width: 100%; height: calc(100% - 70px)">
      <!-- 职业 -->
      <div>
        <div style="height: 100%; width: 100%; overflow-y: auto; z-index: 3" class="flex flex-col items-center">
          <div class="cursor-pointer h-22.5 m-1 w-30 duration-300 job-box box-border relative">
            <div class="text-xs text-center text-white w-full bottom-9.6 justify-center absolute" style="letter-spacing: 10px; text-indent: 10px; z-index: 999" />
            <div class="text-xs text-center w-full bottom-1 text-hex-bea347 absolute">
              {{ name }}
            </div>
            <div class="bg-no-repeat h-full w-full z-2 duration-200 job-border absolute classchange-icon-border" />
            <div :class="['bg-no-repeat bg-auto bg-clip-content h-full w-full z-1 overflow-hidden '].concat([`classchange-icon-${alter_abbr}`])" />
          </div>
        </div>
      </div>
      <div class="w-70% flex justify-center ml-15% min-w-1200px skillinfo">
        <table class="mt-15px" style="font-family: Microsoft YaHei !important; font-size: 15px !important">
          <thead>
            <tr>
              <!-- <th class="w-135px"></th> -->
              <th class="w-300px" :colspan="3">
                <div class="flex w-280px justify-between mx-10px">
                  <div>{{ name }}</div>
                  <div>{{ weapon }}</div>
                  <div>{{ cur_weapon_skill?.type }}</div>
                </div>
              </th>
              <th class="w-65px">
                适用等级
              </th>
              <th class="w-100px">
                等效百分比
              </th>
              <th class="w-65px">
                实际冷却
              </th>
              <th class="w-100px">
                理论秒伤
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in cur_weapon_skill?.skills_active" :key="index" class="h-36px">
              <!-- <th v-if="item.need_level == 100" :rowspan="cur_weapon_skill?.skills_active.filter(a => [50, 85, 100].includes(a.need_level)).length"> 觉醒技能 </th>
              <th
                v-if="index == cur_weapon_skill?.skills_active.findIndex(a => ![50, 85, 100].includes(a.need_level) && (a?.cost ?? 0) > 0 && a.need_level >= 30)"
                :rowspan="cur_weapon_skill?.skills_active.filter(a => ![50, 85, 100].includes(a.need_level) && (a?.cost ?? 0) > 0 && a.need_level >= 30).length"
              >
                中高阶无色
              </th>
              <th
                v-if="index == cur_weapon_skill?.skills_active.findIndex(a => ![50, 85, 100].includes(a.need_level) && (a?.cost ?? 0) == 0 && a.need_level < 40)"
                :rowspan="cur_weapon_skill?.skills_active.filter(a => ![50, 85, 100].includes(a.need_level) && (a?.cost ?? 0) == 0 && a.need_level < 40).length"
              >
                下位技能
              </th> -->
              <th
                v-if="index == cur_weapon_skill?.skills_active.findIndex(a => a.name == item.name) || cur_weapon_skill?.skills_active.filter(a => a.name == item.name).length == 1"
                class="w-40px"
                :rowspan="cur_weapon_skill?.skills_active.filter(a => a.name == item.name).length"
              >
                {{ item.need_level }}
              </th>
              <th
                v-if="index == cur_weapon_skill?.skills_active.findIndex(a => a.name == item.name) || cur_weapon_skill?.skills_active.filter(a => a.name == item.name).length == 1"
                class="w-28px"
                :rowspan="cur_weapon_skill?.skills_active.filter(a => a.name == item.name).length"
              >
                <div :class="`character-icon-${alter_abbr}-${item.name.replace(/[().·，：]+/g, '')}`" />
              </th>
              <th class="w-232px">
                {{ item.name }}{{ item.mode == "" ? "" : " - " }}{{ item.mode }}
              </th>
              <th
                v-if="index == cur_weapon_skill?.skills_active.findIndex(a => a.name == item.name) || cur_weapon_skill?.skills_active.filter(a => a.name == item.name).length == 1"
                :rowspan="cur_weapon_skill?.skills_active.filter(a => a.name == item.name).length"
              >
                <div class="flex items-center w-100% justify-center">
                  <div class="mr-5px">
                    {{ item.lv }}
                  </div><div v-if="item.tp ?? 0 > 0" style="width: 5px; height: 5px; border-radius: 50%; background-color: #3ea74e" />
                </div>
              </th>
              <th>{{ item.data.toFixed(0) }}%</th>
              <th>{{ item.cd.toFixed(1) }}</th>
              <th>{{ (item.data / item.cd).toFixed(0) }}%</th>
            </tr>
          </tbody>
          <template v-if="(cur_weapon_skill?.skills_active.length ?? 0) + 1 < max_cols">
            <tr v-for="index in max_cols - (cur_weapon_skill?.skills_active.length ?? 0) - 1" :key="index" :collapse="8" />
          </template>
        </table>
        <table class="mt-15px right" style="font-family: Microsoft YaHei !important; font-size: 15px !important">
          <thead>
            <tr>
              <th class="w-28px" />
              <th class="w-100px">
                护石技能
              </th>
              <th class="w-65px">
                提升率
              </th>
              <th class="w-80px">
                等效百分比
              </th>
              <th class="w-65px">
                冷却
              </th>
              <th class="w-80px">
                理论秒伤
              </th>
              <th class="w-80px">
                单次提升
              </th>
              <th class="w-80px">
                秒伤提升
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in cur_weapon_skill?.skills_cp.sort((a, b) => b.need_level - a.need_level)" :key="index">
              <th
                v-if="index == cur_weapon_skill?.skills_cp.findIndex(a => a.name == item.name) || cur_weapon_skill?.skills_cp.filter(a => a.name == item.name).length == 1"
                class="w-28px"
                :rowspan="cur_weapon_skill?.skills_cp.filter(a => a.name == item.name).length"
              >
                <div :class="`character-icon-${alter_abbr}-${item.name.replace(/[().·，：]+/g, '')}`" />
              </th>
              <th class="w-150px">
                {{ item.name }}{{ item.mode == "" ? "" : " - " }}{{ item.mode }}
              </th>
              <th class="w-65px">
                {{ `${((item.data / (item.original_data ?? 1) - 1) * 100).toFixed(1)}%` }}
              </th>
              <th class="w-80px">
                {{ `${item.data.toFixed(0)}%` }}
              </th>
              <th class="w-65px">
                {{ item.cd.toFixed(1) }}
              </th>
              <th class="w-80px">
                {{ `${(item.data / item.cd).toFixed(0)}%` }}
              </th>
              <th class="w-80px">
                {{ `${(item.data - (item.original_data ?? 0)).toFixed(0)}%` }}
              </th>
              <th class="w-80px">
                {{ `${(item.data / item.cd - (item.original_data ?? 1) / (item.original_cd ?? 1)).toFixed(0)}%` }}
              </th>
            </tr>
            <template v-if="(cur_weapon_skill?.skills_cp.length ?? 0) + (cur_weapon_skill?.skills_passive.length ?? 0) + 3 < max_cols">
              <tr v-for="item in max_cols - ((cur_weapon_skill?.skills_cp.length ?? 0) + (cur_weapon_skill?.skills_passive.length ?? 0) + 3)" :key="item" :collapse="8" />
            </template>
            <tr>
              <th />
              <th>被动技能&BUFF</th>
              <th>适用等级</th>
              <th>倍率</th>
              <th class="w-65px" :colspan="4">
                说明
              </th>
            </tr>
            <tr v-for="(item, index) in cur_weapon_skill?.skills_passive.sort((a, b) => b.need_level - a.need_level)" :key="index">
              <th
                v-if="index == cur_weapon_skill?.skills_passive.findIndex(a => a.name == item.name) || cur_weapon_skill?.skills_passive.filter(a => a.name == item.name).length == 1"
                class="w-28px"
                :rowspan="cur_weapon_skill?.skills_passive.filter(a => a.name == item.name).length"
              >
                <div :class="`character-icon-${alter_abbr}-${item.name.replace(/[().·，：]+/g, '')}`" />
              </th>
              <th
                v-if="index == cur_weapon_skill?.skills_passive.findIndex(a => a.name == item.name) || cur_weapon_skill?.skills_passive.filter(a => a.name == item.name).length == 1"
                :rowspan="cur_weapon_skill?.skills_passive.filter(a => a.name == item.name).length"
              >
                {{ item.name }}
              </th>
              <th>
                <div class="flex items-center w-100% justify-center">
                  <div class="mr-5px">
                    {{ item.lv }}
                  </div><div v-if="(item?.type ?? '') == 'CDR'" style="width: 5px; height: 5px; border-radius: 50%; background-color: blue" />
                </div>
              </th>
              <th> {{ item.data }}%</th>
              <th :colspan="4">
                {{ item?.remark }}
              </th>
            </tr>
            <tr>
              <th> <div :class="`character-icon-${alter_abbr}-BUFF`" /></th>
              <th>BUFF</th>
              <th>MAX</th>
              <th>{{ cur_weapon_skill?.buff }}</th>
              <th class="w-65px" :colspan="4">
                所有
              </th>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 技能信息 -->
    </div>
  </div>
</template>

<style lang="scss" scoped>
  * {
    text-shadow: none !important;
    user-select: text !important;
  }

  .skillinfo {
    table,
    tr,
    th,
    td {
      font-weight: normal;
      font-family: "Microsoft YaHei" !important;
      font-size: 14px !important;
      div {
        font-weight: normal;
        font-family: "Microsoft YaHei" !important;
        font-size: 14px !important;
      }
    }

    table,
    th,
    td {
      border: 1.5px solid black;
    }

    table {
      border-collapse: collapse;
    }

    .right {
      border-left: none !important;
      th,
      td {
        border-left: none !important;
      }
    }

    tr {
      height: 32px;
    }
  }

  // .ranks {
  //   display: flex;
  //   flex-direction: column;
  //   width: 100%;
  //   height: calc(100% - 60px);
  //   background-repeat: no-repeat;
  //   background-size: cover;
  // }
  // .ranks::after {
  //   content: "";
  //   width: 100%;
  //   height: calc(100% - 34px);
  //   position: absolute;
  //   top: 34px;
  //   left: 0;
  //   background-color: rgba(50, 50, 50, 0.75);
  // }
</style>
