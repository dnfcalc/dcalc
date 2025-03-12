import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
const routes: RouteRecordRaw[] = [
  {
    path: '/:pathMatch(.*)',
    redirect: '/',
  },
  {
    path: '/',
    name: 'home',
    component: defineAsyncComponent(() => import('@/pages/Home/Index.vue')),
  },
  {
    path:'/character/:alter',
    name:'character',
    props: true,
    component: defineAsyncComponent(() => import('@/pages/Character/Index.vue')),
  }
]

const router = createRouter({
  // routes,
  routes,
  history: createWebHistory(import.meta.env.BASE_URL),
})

export default router
