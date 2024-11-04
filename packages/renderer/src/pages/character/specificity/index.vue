<script lang="tsx">
import { defineComponent } from "vue";
// import CnVue from "./cn.vue"
import KrVue from "./kr.vue"
import { useGlobalStore } from "@/store";
import Watermark from "@/components/watermark/index.vue"

export default defineComponent({
  props: {
    simple: {
      type: Boolean,
      default: false
    }
  },
  setup(props) {
    return () => {
      return (
        <>
          <Watermark class="h-100%">
            <KrVue simple={props.simple}/>
          </Watermark>
        </>

      )
    }
  }
})
</script>

<style lang="scss">

</style>
