<template>
  <div class="w-300px">
      <calc-collapse class="w-100%" title="装备打造(点击人物部位切换)">
        <equipment />
      </calc-collapse>
    </div>
</template>
<script setup lang="ts">
import equipment from './components/equipment.vue'
</script>

<style lang="scss">
.equ-profile {
  width: 100%;
  .equ-profile-item {
    width: 100%;
    height: 20px;
    display: flex;
    margin-top: 5px;
    margin-bottom: 5px;
    align-items: center;

    .row-name {
      flex: 0 0 50px;
      text-align: center;
    }

    :not(:last-child) {
      margin-right: 10px !important;
    }

    .i-select-label {
      margin-right: 0px !important;
    }
  }
}
</style>
