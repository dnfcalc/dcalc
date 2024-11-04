import { defineAsyncComponent } from "vue"
import type { RouteRecordRaw } from "vue-router"
import { createRouter, createWebHistory } from "vue-router"

const routes: RouteRecordRaw[] = [
  {
    path: "/:pathMatch(.*)",
    redirect: "/"
  },
  {
    path: "/",
    name: "home",
    component: defineAsyncComponent((() => import("@/pages/home.vue")))
  },
  {
    path: "/auth",
    name: "auth",
    component: defineAsyncComponent((() => import("@/pages/auth.vue")))
  },
  {
    path: "/set",
    name: "set",
    component: defineAsyncComponent(() => import("@/pages/set.vue"))
  },
  {
    path: "/skillinfo",
    name: "skillinfo",
    component: defineAsyncComponent(() => import("@/pages/skillinfo.vue"))
  },
  {
    path: "/character",
    redirect: "/character/singleset",
    name: "main",
    component: defineAsyncComponent(() => import("@/pages/character/main.vue")),
    children: [
      {
        path: "/character/skills",
        name: "skills",
        component: defineAsyncComponent(() => import("@/pages/character/skills/skills.vue")),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/equips",
        name: "equipment",
        component: defineAsyncComponent(() => import("@/pages/character/equipment/equipment.vue")),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/profile",
        name: "profile",
        component: defineAsyncComponent(() => import("@/pages/character/detail/detail.vue")),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/customize",
        name: "customize",
        component: defineAsyncComponent(() => import("@/pages/character/customize/customize.vue")),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/singleset",
        name: "singleset",
        component: defineAsyncComponent(() => import("@/pages/character/singleset/singleset.vue")),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/merge",
        name: "merge",
        component: defineAsyncComponent(() => import("@/pages/character/merge/merge.vue")),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/comparison",
        name: "comparison",
        component: defineAsyncComponent(() => import("@/pages/character/comparison/index.vue")),
        meta: {
          keepAlive: true
        }
      },
      {
        path: "/character/specificity",
        name: "specificity",
        component: defineAsyncComponent(() => import("@/pages/character/specificity/index.vue")),
        meta: {
          keepAlive: true
        }
      }
    ]
  },
  {
    path: "/result",
    name: "result",
    component: defineAsyncComponent(() => import("@/pages/result.vue"))
  },
  {
    path: "/share",
    name: "share",
    component: defineAsyncComponent(() => import("@/pages/character/share/index.vue"))
  },
  {
    path: "/ranking",
    name: "ranking",
    component: defineAsyncComponent(() => import("@/pages/ranking.vue"))
  },
  // {
  //   path: "/rank",
  //   name: "rank",
  //   component: defineAsyncComponent(() => import("@/pages/rank.vue"))
  // },
  {
    path: "/access",
    name: "access",
    component: defineAsyncComponent(() => import("@/pages/access.vue"))
  }
]



const router = createRouter({
  // routes,
  routes,
  history: createWebHistory(import.meta.env.BASE_URL)
})

export default router
