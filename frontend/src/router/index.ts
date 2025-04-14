import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
const routes: RouteRecordRaw[] = [
  // {
  //   path: '/:pathMatch(.*)',
  //   redirect: '/',
  // },
  {
    path: '/',
    name: 'home',
    component: (() => import('@/pages/Home/Index.vue')),
  },
  {
    path:'/character/:alter',
    redirect: (to) => {
      return { path: `/character/equipment/${to.params.alter}` }
    },
    props: true,
    name:'character',
    component: (() => import('@/pages/Character/Index.vue')),
    children: [
      {
        path: '/character/equipment/:alter',
        name: 'equipment',
        props: true,
        component: (() => import('@/pages/Character/EquipmentDictionary/Index.vue')),
      },
      // {
      //   path: '/character/equipment/:alter',
      //   name: 'equipment',
      //   props: true,
      //   component: (() => import('@/pages/Character/Equipment/Index.vue')),
      // },{
      {
        path: '/character/skill/:alter',
        name: 'skill',
        props: true,
        component: (() => import('@/pages/Character/Skill/index.vue')),
      },{
        path: '/character/forge/:alter',
        name: 'forge',
        props: true,
        component: (() => import('@/pages/Character/Forge/index.vue')),
      }
    ]
  }
]

const router = createRouter({
  // routes,
  routes,
  history: createWebHistory(import.meta.env.BASE_URL),
})

export default router
