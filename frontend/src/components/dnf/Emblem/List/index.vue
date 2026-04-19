<template>
  <div class="pos-relative w-248px h-full" :class="props.withBg ? 'emblem-bg' : ''"></div>
</template>

<script lang="ts" setup name="EmblemList">
const props = defineProps({
  withBg: {
    type: Boolean,
    default: true,
  },
  detail: {
    type: Object as PropType<Record<string, any>>,
  },
})
</script>

<style lang="scss" scoped>
.emblem-bg {
  background-image: url(../Images/head.png);
}
</style>
