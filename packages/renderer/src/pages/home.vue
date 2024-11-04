<script lang="tsx">
import { computed, defineComponent, onMounted, onUnmounted, ref, renderList } from "vue"
import Update from "./update.vue"
import api from "@/api"
import type { IAlterInfo } from "@/api/info/type"
import { useDialog } from "@/components/hooks/dialog"
import { useOpenWindow } from "@/hooks/open"
import { sleep } from "@/utils/sync"
import { useAppStore } from "@/store"
import { decrypt, getSession } from "@/utils"

function job_icon(child: IAlterInfo) {
  return {
    filter: !(child.open || import.meta.env.DEV) ? "grayscale(100%)" : ""
  }
}

export default defineComponent(async () => {
  const { alert, show, close, randomId } = useDialog()
  const openUrl = useOpenWindow()

  const checkUpdate = ref(0)
  if (window.pywebview) {
    const globalSet = await api.getGlobalDetail()
    checkUpdate.value = (globalSet?.[0] ?? 0) as number
  } else {
    checkUpdate.value = 1
  }

  function getProfiles() {
    // 遍历localStorage，判断是否有旧版数据,根据 dcalc/${job}/sets和dcalc/${job}/favorites的规则判断

    const profiles: [string, string][] = []

    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i)
      if (key?.startsWith("dcalc/") && !key.endsWith("/access_token")) {
        try {
          const value = JSON.parse(localStorage.getItem(key) ?? "")
          if (value) {
            profiles.push([key, value])
          }
        } catch { }
      }
    }
    return profiles
  }

  async function handleLogin() {
    if (window.pywebview) {
      return alert({
        content: "请在网页版中使用登录功能"
      })
    }

    const loginListener = async (event: MessageEvent) => {
      if (event.data.tag === "dcalc" && event.data.type === "login") {
        const { data } = event.data
        if (data) {
          localStorage.setItem("dcalc/access_token", data)
          await sleep(400)
          if (window.pywebview) {
            await show({
              content: "登录成功，是否导入本地数据？",
              okButton: "导入",
              cancelButton: "取消",
              rejectButton: false
            })
          } else {
            const profiles = getProfiles()
            if (profiles.length > 0) {
              const rs = await show({
                content: "登录成功，是否导入本地数据？",
                okButton: "导入",
                cancelButton: "取消",
                rejectButton: false
              })
              if (rs.isOk) {
                await api.importConfigs(Object.fromEntries(profiles))
              }
            }
          }
        }
      }
    }
    window.addEventListener("message", loginListener)
    await openUrl("https://api.dnftools.com/auth/login", { width: 1100, height: 750, title: "登录" })
    window.removeEventListener("message", loginListener)
  }

  const ignores = ["empty"]
  const zoom = computed(() => /android|webos|iphone|ipad|ipod|blackberry|iemobile|opera mini/i.test(navigator.userAgent || navigator.vendor || (window as any).opera) ? 1 : Math.max(Math.min((window.innerHeight * 0.8 / 750), (window.innerWidth * 0.85 / 1100)), 1))


  const showDetail = computed(() => {
    return (useAppStore().userInfo?.show ?? false)
  })

  // 获取角色相关信息，判定是否开放
  function choose_job(child: IAlterInfo) {
    return async () => {
      if (child.comment == "首页") {
        return openUrl("https://dnftools.com/")
      }
      if (child.comment == "设置") {
        return openUrl("/set", { width: 600, height: 500, scale: zoom.value })
      }
      if (ignores.includes(child.name)) {
        return
      }

      // if (child.open || child.url) {
      //   await openUrl()
      // } else {
      //   await alert({
      //     content: "未开放的角色!"
      //   })
      // }
      if (ignores.includes(child.name)) {
        return
      }
      if (child.name == "sponsor") {
        return openUrl(child.url ?? "")
      }
      if (child.name == "login" && child.url) {
        return handleLogin()
      }



      if (child.open || import.meta.env.DEV) {
        const options = child.options ?? []
        if (options.length > 0) {
          const id = randomId()
          return await show({
            // id,
            scale: zoom.value,
            content: "请选择职业平衡版本",
            action: () => {
              return (
                <div class="flex items-center justify-around flex-wrap" style="width:200px">
                  {renderList(options, option =>
                    !option.class ? (
                      <calc-button class="!w-40% !mb-2" disabled={(option.class?.includes("HF.") || option.class?.includes("crusader_female_carry") || option.class?.includes("enchantress_carry")) && showDetail.value}
                        onClick={() => {
                          if (((option.class?.includes("HF.") || option.class?.includes("crusader_female_carry") || option.class?.includes("enchantress_carry")) && !showDetail.value)) {
                            return
                          }
                          openUrl("/character", { query: { alter: child.name }, width: 1100, height: 775, scale: zoom.value })
                          close(id, "ok")
                        }}
                      >
                        {option.title}
                      </calc-button>
                    ) : (
                      <calc-button class="!w-40% !mb-2" disabled={(option.class?.includes("HF.") || option.class?.includes("crusader_female_carry") || option.class?.includes("enchantress_carry")) && !showDetail.value}
                        onClick={() => {
                          if (((option.class?.includes("HF.") || option.class?.includes("crusader_female_carry") || option.class?.includes("enchantress_carry")) && !showDetail.value)) {
                            return
                          }
                          openUrl("/character", { query: { alter: option.class ?? "" }, width: 1100, height: 775, scale: zoom.value })
                          close(id, "ok")
                        }}
                      >
                        {option.title}
                      </calc-button>
                    )
                  )}
                </div>
              )
            }
          })
        }
        return openUrl("/character", { query: { alter: child.name }, width: 1100, height: 775, title: child.title, scale: zoom.value })
      } else {
        return alert({
          content: "未开放的角色!"
        })
      }
    }
    // router.push("/character/" + alter)
  }


  const canClick = ref(true)
  const visible = ref(true)

  let checkTimer: NodeJS.Timeout

  onMounted(async () => {
    checkTimer = setTimeout(() => {
      canClick.value = false
    }, 5000)
    window.removeLoading()
    useAppStore().uid = decrypt(await getSession("uid"))?.uid ?? -1
  }
  )

  const closeWindow = ()=>{
    console.log(window.pywebview)
    if(!!window.pywebview){
      window.pywebview.api.invoke("close-win");
    }
    else{
      openUrl(`https://dnftools.com`, { target: "_self" })
    }
  }

  const adventure = await api.adventures().then(r => r.data)
  const tools = (await api.tools().then(r => r.data)).filter(a => a.end == undefined || new Date(a.end) > new Date())

  const app = useAppStore()
  const infos = computed(() => {
    return (app.userInfo?.uid ?? -1) > 0 ? `${app.userInfo.userName ?? ""}(${app.userInfo.uid})<br/>${app.userInfo.show ? "可正常使用功能" : `${app.userInfo.reason},限制使用`}` : "点击同步colg登录信息<br/>可解锁更多功能"
  })
  // function getName(name: string) {
  //   return ignores.includes(name) ? "" : name
  // }

  return () => (
    <>
      <div class="bg-cover bg-no-repeat h-auto min-h-full pt-8 pb-12 pl-4 home" style={`zoom:${zoom.value};background-image: url('${import.meta.env.BASE_URL}images/home.jpg')`}>
        {!checkUpdate.value && <Update />}
        {
          <calc-dialog close-button={false} header="用户须知" visible={visible.value} scale={zoom.value} mask={true}>
          <div class="flex flex-col py-2 px-4 items-center justify-center bg-black">
            <div>1、请勿用于打桩排名等节奏行为。</div>
            <div>2、不授权任何使用计算器做打桩排名的行为。</div>
            <div>3、伤害数字需在右上角同步colg登录并达到高级用户。</div>
            <div>4、风雨烟云、煮酒忘忧等DJ及其支持者请勿使用。</div>
            <div class="w-100% mt-10px flex justify-around">
              <calc-button onClick={()=>visible.value=false}>
                  已知悉
              </calc-button>
              <calc-button onClick={closeWindow}>
                  不同意
              </calc-button>
            </div>
          </div>
        </calc-dialog>
        }
        {renderList(adventure, job => (
          <div class="flex flex-row">
            <div class="bg-no-repeat bg-center flex flex-wrap h-25 w-30 job-icon-box justify-center items-center relative character-icon-flash">
              <div class={["bg-center bg-no-repeat h-22.5 w-30"].concat(`character-icon-${job.name}`)}></div>
            </div>
            {renderList(job.children, child => (
              <div onClick={choose_job(child)} class="cursor-pointer h-22.5 m-1 w-30 duration-300 job-box box-border relative">
                {child.open && child.name != "sponsor" && <div class="bg-no-repeat h-full w-full z-2 duration-200 job-border absolute classchange-icon-border hover:bg-hex-ffd7002e"></div>}
                <div class="text-xs text-center text-white w-full bottom-9.6 justify-center absolute" style="letter-spacing:10px;text-indent:10px;z-index:999">
                  {child.comment}
                  {/* {window.pywebview ? child.comment : ""} */}
                </div>
                <div class="text-xs text-center w-full bottom-1 text-hex-bea347 absolute">{child.title}</div>
                <div class={["bg-no-repeat bg-auto bg-clip-content h-full w-full z-1 overflow-hidden "].concat([`classchange-icon-${child.name}`])} style={job_icon(child)}></div>
              </div>
            ))}
          </div>
        ))}
        <div v-show={!window.pywebview} class="flex pt-4 justify-center">
          <a class="text-hex-bea347" href="https://beian.miit.gov.cn/" target="_blank">
            赣ICP备2023003492号
          </a>
        </div>
      </div>

      <div
        class="flex flex-col"
        onClick={() => openUrl(`https://bbs.colg.cn/zfj_auth.html?r=${Date.now().toString()}`, { target: "_self" })}
        style={`position: absolute;top: ${30 + 82 * 0}px;left: 750px;width: 160px;height: 150px;zoom:${zoom.value}`}>
        <div class="w-70px h-50px bg-no-repeat" style={`z-index:5;background-position:2% 50%;background-size:100% auto;background-image: url('${import.meta.env.BASE_URL}images/tooltips/login.gif')`}></div>
        <div v-html={infos.value} style={`background-image: url('${import.meta.env.BASE_URL}images/login.png');color:#bea347;text-align:center;background-size:100% auto;position:relative;top:-10px`} class="bg-no-repeat h-65px w-100% flex items-center justify-center ">

        </div>
      </div>

      {renderList(tools, (tool, index) => (
        <div
          class="flex"
          v-show={!window.pywebview}
          style={`background-image: url('${import.meta.env.BASE_URL}images/tooltips.png');position: absolute;top: ${50 + 82 * (index + 2)}px;left: 750px;width: 227px;height: 82px;zoom:${zoom.value}`}
          onClick={() => openUrl(tool.link, { target: tool.target })}
        >
          <div class="w-70px h-100% bg-no-repeat" style={`background-position:70% 40%;background-image: url('${import.meta.env.BASE_URL}images/tooltips/${index}.gif')`}></div>
          <div v-html={tool.tooltips} class="h-100% w-145px flex items-center justify-center" style="color:#bea347;text-align:center"></div>
        </div>
      ))}
    </>
  )
})
</script>

<style lang="scss">
.home {
  // background-image: url($path + "bg.jpg");
  background-size: 100% 100%;

  // .job-icon-box {
  //   // background-image: url($path + "flash.png");
  // }

  // .job-box {
  //   .job-border {
  //     // background-image: url($path + "border.png");
  //   }
  // }
}
</style>
