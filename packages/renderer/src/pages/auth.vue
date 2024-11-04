<template>
  <div style="display: none;">当前用户：{{userInfo?.userName}}</div>
  </template>

  <script setup lang="ts">

  import { useAppStore } from '@/store';
  import { decrypt, resetSetItem } from '@/utils';
  import { useRouter, useRoute } from 'vue-router'

  import axios from "axios"
  // import { computed } from 'vue';

  const instance = axios.create({
    timeout: 1000,
  })

  const route = useRoute();
  const router = useRouter();
  const uid = (route.query?.uid ?? -1).toLocaleString()

  const info = decrypt(decodeURIComponent(uid))
  if(parseInt(Date.now().toString()) - info.time > 5 * 1000 || parseInt(Date.now().toString()) - info.time < 0){
    window.alert("登录超时")
    router.push({name: 'home'})
  }
  else{
    try {
      resetSetItem("uid",(route.query?.uid ?? -1).toLocaleString())
      instance.get(`http://127.0.0.1:17173/api/uid/set/${uid}`).then(a=>{
        var userConfirmation = window.confirm("检测到正在运行桌面端，是否唤起桌面端")
        if(userConfirmation){
          location.replace("dcalc://reloadApp?uid="+uid)
          router.push({name: 'home'})
        }
        else{
          throw "请在桌面端打开"
        }
      }).catch(e=>{
        router.push({name: 'home'})
      })
    }catch (e) {
      router.push({name: 'home'})
    }

  }

  </script>
