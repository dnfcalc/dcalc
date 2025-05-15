<template>
  <calc-cascader
    class="!h-5 flex-1"
    v-model="selected"
    :items="items"
    placeholder="请输入名称搜索"
  ></calc-cascader>
</template>

<script lang="ts" setup>
import type { TreeNode } from '@/components/calc/tree/types'
import { useInfoStore } from '@/stores'
import { syncRef, useVModel } from '@vueuse/core'

const props = defineProps({
  partList: {
    type: Array as () => String[],
    default: () => [],
  },
})

const armor_parts = ['上衣', '头肩', '下装', '鞋', '腰带']

const jewel_parts = ['项链', '戒指', '手镯']

const special_parts = ['辅助装备', '魔法石', '耳环']

const else_parts = ['称号', '宠物']

const emit = defineEmits([])

const choose_part = useVModel(props, 'partList', emit, { passive: true })

const selected = ref('')

const infoStore = useInfoStore()

const items = computed<TreeNode[]>(() => {
  return [
    {
      label: '全部类别',
      value: '',
      onSelect() {
        choose_part.value = []
      },
    },
    {
      label: '武器',
      value: '武器',
      onSelect() {
        choose_part.value = infoStore.infos?.weapons ?? []
      },
      children: infoStore.infos?.weapons.map((r) => {
        return {
          label: r,
          value: r,
          onSelect() {
            choose_part.value = [r]
          },
        }
      }),
    },
    {
      label: '防具',
      value: '防具',
      onSelect() {
        choose_part.value = [...armor_parts]
      },
      children: armor_parts.map((part) => {
        return {
          label: part,
          value: part,
          onSelect() {
            choose_part.value = [part]
          },
        }
      }),
    },
    {
      label: '首饰',
      value: '首饰',
      onSelect() {
        choose_part.value = [...jewel_parts]
      },
      children: jewel_parts.map((part) => {
        return {
          label: part,
          value: part,
          onSelect() {
            choose_part.value = [part]
          },
        }
      }),
    },
    {
      label: '特殊装备',
      value: '特殊装备',
      onSelect() {
        choose_part.value = [...special_parts]
      },
      children: special_parts.map((part) => {
        return {
          label: part,
          value: part,
          onSelect() {
            choose_part.value = [part]
          },
        }
      }),
    },
    {
      label: '其它',
      value: '其它',
      onSelect() {
        choose_part.value = [...else_parts]
      },
      children: else_parts.map((part) => {
        return {
          label: part,
          value: part,
          onSelect() {
            choose_part.value = [part]
          },
        }
      }),
    },
  ]
})
</script>
