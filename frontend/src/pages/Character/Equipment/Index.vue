<template>
  <div class="mx-10px">
    <calc-collapse title="武器/称号/宠物/秘宝">
      <calc-tabs v-model="anotherTab" class="!mb-2">
        <calc-tab :value="0">武器</calc-tab>
        <calc-tab :value="1">称号/宠物/秘宝</calc-tab>
        <calc-tab :value="2" v-if="infoStore.infos?.alter.includes('vegabond')">副武器</calc-tab>
      </calc-tabs>
      <Weapon v-show="anotherTab === 0"></Weapon>
      <Else v-show="anotherTab === 1"></Else>
      <SubWeapon v-show="anotherTab === 2"></SubWeapon>
    </calc-collapse>
    <calc-collapse title="套装/通宝">
      <calc-tabs v-model="equTab" class="!mb-2">
        <calc-tab :value="0">套装</calc-tab>
        <calc-tab :value="1">通宝</calc-tab>
      </calc-tabs>
      <Suit v-show="equTab === 0"></Suit>
      <Universal v-show="equTab === 1"></Universal>
    </calc-collapse>
    <calc-collapse title="融合石">
      <calc-tabs v-model="stoneTab" class="!mb-2">
        <calc-tab :value="0">套装</calc-tab>
        <calc-tab :value="1">通宝</calc-tab>
        <calc-tab :value="2">其他</calc-tab>
      </calc-tabs>
      <Stone v-show="stoneTab == 0"></Stone>
      <StoneUniversal v-show="stoneTab == 1"></StoneUniversal>
      <StoneOld v-show="stoneTab == 2"></StoneOld>
    </calc-collapse>
  </div>
</template>

<script lang="ts" setup name="Index">
import Suit from './components/Suit.vue'
import Weapon from './components/Weapon.vue'
import Stone from './components/Stone.vue'
import Universal from './components/Universal.vue'
import StoneUniversal from './components/StoneUniversal.vue'
import StoneOld from './components/StoneOld.vue'
import Else from './components/Else.vue'
import { useInfoStore } from '@/stores'
import SubWeapon from './components/SubWeapon.vue'

const infoStore = useInfoStore()
const equTab = ref(0)
const stoneTab = ref(0)
const anotherTab = ref(0)
</script>
