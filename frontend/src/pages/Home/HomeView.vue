<script lang="tsx">
import { Fragment, computed, defineComponent, onMounted, ref, renderList } from 'vue'
import api from '@/api'
import type { IAlterInfo } from '@/api/info/type'
import { getImageURL } from '@/utils/images'

function job_icon(child: IAlterInfo) {
  return {
    filter: !(child.open || import.meta.env.DEV) ? 'grayscale(100%)' : '',
    backgroundImage: `url('${getImageURL(`adventure/jobs/${child.name}.png`)}')`,
  }
}

export default defineComponent(async () => {
  const ignores = ['empty']
  const zoom = computed(() =>
    /android|webos|iphone|ipad|ipod|blackberry|iemobile|opera mini/i.test(
      navigator.userAgent || navigator.vendor || (window as any).opera,
    )
      ? 1
      : Math.max(Math.min((window.innerHeight * 0.8) / 750, (window.innerWidth * 0.85) / 1100), 1),
  )

  // 获取角色相关信息，判定是否开放
  function choose_job(child: IAlterInfo) {
    return async () => {
      // if (child.comment == '首页') {
      //   return openUrl('https://dnftools.com/')
      // }
      // if (child.comment == '设置') {
      //   return openUrl('/set', { width: 600, height: 500, scale: zoom.value })
      // }
      // if (ignores.includes(child.name)) {
      //   return
      // }
      // if (child.name == 'sponsor') {
      //   return openUrl(child.url ?? '')
      // }
      // if (child.open || import.meta.env.DEV) {
      //   const options = child.options ?? []
      //   if (options.length > 0) {
      //     const id = randomId()
      //     return await show({
      //       // id,
      //       scale: zoom.value,
      //       content: '请选择职业平衡版本',
      //       action: () => {
      //         return (
      //           <>
      //             <div class="flex items-center justify-around flex-wrap" style="width:200px">
      //               {renderList(options, (option) =>
      //                 !option.class ? (
      //                   <calc-button
      //                     class="!w-40% !mb-2"
      //                     onClick={() => {
      //                       openUrl('/character', {
      //                         query: { alter: child.name },
      //                         width: 1100,
      //                         height: 775,
      //                         scale: zoom.value,
      //                       })
      //                       close(id, 'ok')
      //                     }}
      //                   >
      //                     {option.title}
      //                   </calc-button>
      //                 ) : (
      //                   <calc-button
      //                     class="!w-40% !mb-2"
      //                     onClick={() => {
      //                       openUrl('/character', {
      //                         query: { alter: option.class ?? '' },
      //                         width: 1100,
      //                         height: 775,
      //                         scale: zoom.value,
      //                       })
      //                       close(id, 'ok')
      //                     }}
      //                   >
      //                     {option.title}
      //                   </calc-button>
      //                 ),
      //               )}
      //             </div>
      //           </>
      //         )
      //       },
      //     })
      //   }
      //   return openUrl('/character', {
      //     query: { alter: child.name },
      //     width: 1100,
      //     height: 775,
      //     title: child.title,
      //     scale: zoom.value,
      //   })
      // } else {
      //   return alert({
      //     content: '未开放的角色!',
      //   })
      // }
    }
    // router.push("/character/" + alter)
  }

  // const canClick = ref(true)

  // let checkTimer: NodeJS.Timeout

  const adventure = await api.adventures()

  return () => (
    <Fragment>
      <div class="bg-no-repeat h-auto min-h-full pt-8 pb-12 pl-4" style={`zoom:${zoom.value};background-image: url('${getImageURL('home.jpg')}');background-size: 100% 100%;`}>
        {renderList(adventure, (job) => (
          <div class="flex flex-row">
            <div
              class="bg-no-repeat bg-center flex flex-wrap h-25 w-30 job-icon-box justify-center items-center relative character-icon-flash"
              style={`background-image:url('${getImageURL('adventure/sub/flash.png')}')`}
            >
              <div
                class="bg-center bg-no-repeat h-22.5 w-30"
                style={`background-image:url('${getImageURL(`adventure/sub/${job.name}.png`)}')`}
              ></div>
            </div>
            {renderList(job.children, (child) => (
              <div
                onClick={choose_job(child)}
                class="cursor-pointer h-22.5 m-1 w-30 duration-300 job-box box-border relative"
              >
                {child.open && child.name != 'sponsor' && (
                  <div
                    class="bg-no-repeat h-full w-full z-2 duration-200 job-border absolute hover:bg-hex-ffd7002e"
                    style={`background-image:url('${getImageURL('adventure/jobs/border.png')}')`}
                  ></div>
                )}
                <div
                  class="text-xs text-center text-white w-full bottom-9.6 justify-center absolute"
                  style="letter-spacing:10px;text-indent:10px;z-index:999"
                >
                  {child.comment}
                </div>
                <div class="text-xs text-center w-full bottom-1 text-hex-bea347 absolute">
                  {child.title}
                </div>
                <div
                  class="bg-no-repeat bg-auto bg-clip-content h-full w-full z-1 overflow-hidden"
                  style={job_icon(child)}
                ></div>
              </div>
            ))}
          </div>
        ))}
        <div class="flex pt-4 justify-center">
          <a class="text-hex-bea347" href="https://beian.miit.gov.cn/" target="_blank">
            赣ICP备2023003492号
          </a>
        </div>
      </div>

      <div
        class="flex flex-col"
        style={`position: absolute;top: ${30 + 82 * 0}px;left: 775px;width: 160px;height: 150px;zoom:${zoom.value}`}
      >
        <div
          class="w-70px h-50px bg-no-repeat"
          style={`z-index:5;background-position:2% 50%;background-size:100% auto;background-image: url('${import.meta.env.BASE_URL}images/tooltips/login.gif')`}
        ></div>
      </div>
    </Fragment>
  )
})
</script>

<style lang="scss"></style>
