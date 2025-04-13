<template>
  <div>
    <!-- 头部 选择是装备还是融合石 -->
    <div class="flex">
      <div :class="{active: category === 'equ'}">装备</div>
      |
      <div :class="{active: category === 'stone'}">融合石</div>
    </div>
    <!-- 筛选条件 -->
    <!-- 装备列表 -->
  </div>


</template>
<script lang="ts">
const category = ref("equ")

</script>
