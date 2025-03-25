import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import vueDevTools from 'vite-plugin-vue-devtools'
import Components from 'unplugin-vue-components/vite'
import AutoImport from 'unplugin-auto-import/vite'
import RekaResolver from 'reka-ui/resolver'
import UnoCSS from 'unocss/vite'
import uncomponents from "unplugin-vue-components/vite"

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
    // vueDevTools(),
    UnoCSS(),
    uncomponents({
      dts: true,
      dirs: ["src/components/"],
      allowOverrides: true,
      directoryAsNamespace: true
    }),
    Components({
      dts: 'src/types/components.d.ts',
      resolvers: [RekaResolver()],
    }),
    AutoImport({
      imports: ['vue', 'vue-router', '@vueuse/core'],
      include: [
        /\.[tj]sx?$/, // .ts, .tsx, .js, .jsx
        /\.vue$/,
        /\.vue\?vue/, // .vue
      ],
      dts: 'src/types/auto-imports.d.ts', // specify the dts file path
      // 解决eslint报错问题
      eslintrc: {
        // 这里先设置成true然后npm run dev 运行之后会生成 .eslintrc-auto-import.json 文件之后，在改为false
        enabled: true,
        filepath: './.eslintrc-auto-import.json', // 生成的文件路径
        globalsPropValue: true,
      },
    }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})
