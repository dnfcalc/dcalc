import { onBeforeUnmount } from "vue";
export const getMark = () => {
  /**
   * 设置水印方法
   * @param {string} str - 输出文本
   * @param {HTMLElement} [container] - 设置水印的容器(如果不写则默认设置全屏水 印)
   * @param {boolean} [createTime] - 水印生成时间
   */
  const setWaterMark = (
    str: string,
    createTime: boolean,
    container?: HTMLElement
  ) => {
    // 创建唯一标识符id
    const dpr = window.devicePixelRatio
    const id = "1.23452384164.123412416";
    if (document.getElementById(id) !== null) {
      container
        ? container.removeChild(document.getElementById(id)!)
        : document.body.removeChild(document.getElementById(id)!);
    }
    // 创建画布
    const can = document.createElement("canvas");
    // 设置画布长宽
    can.width = 120;
    can.height = 90;
    // 获取画布元素2D渲染上下文
    const cans = can.getContext("2d")!;
    // 设置旋转角度(逆时针旋转15度)
    cans.rotate((-20 * Math.PI) / 180);
    // 设置字体
    cans.font = "15px SimSun";
    // 设置填充绘色
    cans.fillStyle = "rgba(200, 200, 200, 0.35)";
    // 设置在绘制文本时使用当前文本基线
    cans.textBaseline = "middle";
    /**
     * 在画布上绘制填色文本
     * @param {string} str - 输出文本
     * @param {number} width - 开始绘制文本X坐标位置
     * @param {number} height - 开始绘制文本Y坐标位置
     */
    cans.fillText(str, can.width / 10, can.height / 1.5);
    if (createTime) {
      // 获取当前时间并格式化
      const curDate = new Date();
      const dateStr = curDate.toLocaleDateString();
      const timeStr = curDate.toLocaleTimeString();
      const timeStamp = `${dateStr} ${timeStr}`;
      const timeTextWidth = cans.measureText(timeStamp).width;
      const timeTextX = (can.width - timeTextWidth) / 2;
      cans.font = "15px Vedana";
      cans.fillText(timeStamp, timeTextX, (can.height / 3) * 2);
    }
    // 创建全屏浮动全屏浮动div, 将画布作为背景
    const div = document.createElement("div");
    div.id = id;
    div.style.pointerEvents = "none";
    div.style.top = "15px";
    div.style.left = "0px";
    div.style.position = "absolute";
    div.style.zIndex = "0";
    div.style.width = container ? `${container.clientWidth}px` : "100%";
    div.style.height = container ? `${container.clientHeight}px` : "100%";
    div.style.background = `url(${can.toDataURL("image/png")}) left top repeat`;
    if (container) {
      container.style.position = "relative";
      container.appendChild(div);
    } else {
      document.body.appendChild(div);
    }

    return id;
  };

  // 只允许调用一次该方法
  const waterMark = (
    str: string,
    createTime: boolean,
    container?: HTMLElement
  ) => {
    let id = setWaterMark(str, createTime, container);
    // 定时检查是否存在具有相同标识符的元素
    setInterval(() => {
      if (document.getElementById(id) === null) {
        id = setWaterMark(str, createTime, container);
      }
    }, 500);

    // 监听窗口大小调整, 确保水印的适应性
    const handleResize = () => {
      setWaterMark(str, createTime, container);
    };
    const observer = new ResizeObserver(handleResize);
    // 全屏监听
    if (!container) {
      observer.observe(document.documentElement, { box: "content-box" });
    }
    // 指定容器监听
    else {
      observer.observe(container, { box: "content-box" });
    }

    // 组件销毁时清除监听
    onBeforeUnmount(() => {
      observer.disconnect();
    });
  };
  return { waterMark };
};
