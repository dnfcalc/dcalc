<script lang="tsx">
import { defineComponent, onMounted } from "vue"
import { useRoute } from "vue-router"
import { useAppStore } from "@/store"

export default defineComponent(() => {
  const route = useRoute()
  const appStore = useAppStore()
  onMounted(() => {
    const token = route.query.access_token as string
    if (token) {
      window.parent.postMessage(
        {
          tag: "dcalc",
          type: "login",
          data: token
        },
        "*"
      )
      appStore.close()
    }
  })
  return () => <div></div>
})
</script>
