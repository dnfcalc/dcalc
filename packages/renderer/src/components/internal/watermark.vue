<script lang="tsx">
import { defineComponent, onMounted, ref } from "vue"

function mergeData(ctx: CanvasRenderingContext2D, textData: ImageData, color: "R" | "G" | "B", originalData: ImageData) {
  const oData = originalData.data
  const newData = textData.data
  let bit: number, offset: number // offset的作用是找到结合bit找到对应的A值，即透明度

  switch (color) {
    case "R":
      bit = 0
      offset = 3
      break
    case "G":
      bit = 1
      offset = 2
      break
    case "B":
      bit = 2
      offset = 1
      break
  }

  for (let i = 0; i < oData.length; i++) {
    // 此处是为了筛选我们要修改的RGB中那一项，在此处，过滤出来的就是每个坐标点的R值
    if (i % 4 == bit) {
      // 我们获取到R值的位置，那对应这个点的A值就是i+offset
      if (newData[i + offset] === 0 && oData[i] % 2 === 1) {
        // 此处先判断该坐标点的透明度，如果为0，说明这个点是没有水印的，将没有水印信息点的R值变为偶数，并且不能超过0-255的范围
        if (oData[i] === 255) {
          oData[i]--
        } else {
          oData[i]++
        }
      } else if (newData[i + offset] !== 0 && oData[i] % 2 === 0) {
        // 透明度非0，该点有信息，若该点的R值是偶数，将其改为奇数
        oData[i]++
      }
    }
  }
  // 至此，整个图片中所有包含水印信息的点的R值都是奇数，没有水印信息的点的R值都是偶数，再将图片绘入画布，即完成整个水印添加过程
  ctx.putImageData(originalData, 0, 0)
}
export default defineComponent({
  props: {
    src: {
      type: String,
      required: true
    },
    content: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const canvasRef = ref<HTMLCanvasElement>()

    onMounted(() => {
      const canvas = canvasRef.value
      if (canvas) {
        const ctx = canvas.getContext("2d")
        const img = new Image()
        let textData, originalData

        img.src = props.src
        // 图片加载完成
        img.onload = function () {
          if (!ctx) {
            return
          }
          // 设置画布宽高为图片宽高
          canvas.width = img.width
          canvas.height = img.height
          // console.log(canvas)
          // 设置水印字体
          ctx.font = "30px Microsoft Yahei"
          //   ctx.fillStyle = "color:#fff"
          // 由于图片宽度固定为800，我们需要在每一行添加三个水印,每隔100像素新增一行水印
          for (let i = 0; i < canvas.height; i += 40) {
            for (let j = 0; j < canvas.width; j += 40) {
              ctx.fillText(props.content, j, i)
            }
          }

          // 此时画布上已经有了水印的信息，我们获取水印的各个像素的信息
          textData = ctx.getImageData(0, 0, ctx.canvas.width, ctx.canvas.height)
          // 将图片绘入画布
          ctx.drawImage(img, 0, 0, canvas.width, canvas.height)
          // 获取图片各个像素点的信息，将originalData打印出来，会发现是一个非常大的数组（由于文字和图片在同一块画布，因此textData的长度等于originalData长度）
          // 这个数组的长度等于图片width*height*4，即图片像素宽乘以高乘以4，0-3位是第一个点的RGBA值，第4-7位是第二个点的RGBA值，以此类推
          originalData = ctx.getImageData(0, 0, ctx.canvas.width, ctx.canvas.height)
          // 调用盲水印算法
          mergeData(ctx, textData, "R", originalData)
        }
      }
    })

    return () => <canvas class="  pointer-events-none" ref={canvasRef} />
  }
})
</script>
