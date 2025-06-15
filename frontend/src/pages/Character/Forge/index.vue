<template>
  <div class="w-420px overflow-auto">
    <calc-collapse class="w-100%" title="装备/时装打造(点击部位切换)">
      <calc-tabs v-model="partTab" class="!mb-2">
        <calc-tab :value="0">装备栏</calc-tab>
        <calc-tab :value="1">时装栏</calc-tab>
      </calc-tabs>
      <equipment v-if="partTab === 0"></equipment>
      <clothes v-if="partTab === 1"></clothes>
    </calc-collapse>
    <calc-collapse class="w-100%" title="辟邪玉">
      <jade></jade>
    </calc-collapse>
    <calc-collapse class="w-100%" title="其它">
      <sundry></sundry>
    </calc-collapse>
  </div>
</template>
<script setup lang="ts">
import equipment from './components/Equipments.vue'
import clothes from './components/Avatars.vue'
import jade from './components/Jades.vue'
import sundry from './components/Sundry.vue'
const partTab = ref(0)
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
