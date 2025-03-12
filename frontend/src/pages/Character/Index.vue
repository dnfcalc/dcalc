<template>
  <div class="h-90vh w-560px overflow-y-auto overflow-x-hidden">
    <SkillTree></SkillTree>
  </div>

</template>

<script lang="ts" setup name="Index">
import { useInfoStore } from '@/stores/info'
import { getImageURL } from '@/utils/images'
import SkillTree from './Skill/SkillTree.vue';
const props = defineProps<{
  alter: string
}>()
const infoStore = useInfoStore()
onMounted(() => {
  infoStore.createCharacter(props.alter, '0')
})
</script>
