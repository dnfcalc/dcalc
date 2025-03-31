<template>
  <div class="w-full overflow-y-auto mt-0 h-100%">
    <Suspense>
      <RouterView></RouterView>
    </Suspense>
    <render/>
  </div>
</template>

<script lang="ts" name="index" setup>
import { useDialog } from '@/components/hooks/dialog';

const { render } = useDialog()
</script>
