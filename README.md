## 简介

web:vue3+TS+electron+vite<br> 参考项目：https://github.com/caoxiemeihao/electron-vue-vite <br>使用拖拽组件：https://github.com/SortableJS/vue.draggable.next <br> api:python+FastAPI

## 联系

Email:wxh_email@yeah.net

## 项目依赖安装

先安装好 python3.6 以上、node 16 以上 以及 Git

```
    npm config --global set registry https://registry.npmmirror.com/

    npm install -g pnpm

    git clone https://gitee.com/dcalc/dnfcalculating_110.git

    cd ./dnfcalculating_110

    pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ -r requirements.txt

    pnpm install

    若安装node_modules/.pnpm/electron时超时失败可尝试换源

    pnpm config set electron_mirror "https://npm.taobao.org/mirrors/electron/"

```

## 项目运行

```
  pnpm dev:app
```
