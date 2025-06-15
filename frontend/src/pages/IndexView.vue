<template>
  <div class="w-full overflow-y-auto mt-0 h-100%" :style="`zoom:${zoom}`">
    <Suspense>
      <RouterView></RouterView>
    </Suspense>
    <render />
  </div>
</template>

<script lang="ts" name="index" setup>
const zoom = computed(() => {
  const DPI = /macintosh|mac os x/i.test(navigator.userAgent.toLowerCase()) ? 1 : window.devicePixelRatio || 1;
  return /android|webos|iphone|ipad|ipod|blackberry|iemobile|opera mini/i.test(navigator.userAgent || navigator.vendor || (window as any).opera) ? 1 :(window.screen.width / 1800 / 0.85 / DPI).toFixed(2)
})
import { useDialog } from '@/components/hooks/dialog'

const { render } = useDialog()
</script>
