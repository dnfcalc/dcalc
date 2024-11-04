import path from "node:path"
import jsx from "@vitejs/plugin-vue-jsx"
import vue from "@vitejs/plugin-vue"
import unocss from "unocss/vite"
import { createSprite2CssPlugin } from "@curev/vite-plugin-sprite"
import uncomponents from "unplugin-vue-components/vite"
import { defineConfig } from "vite"
import fs from "fs-extra"
import viteCompression from "vite-plugin-compression"

import { presetUno } from "unocss"
import pkg from "../../package.json"

// vite build ./packages/renderer --base /dcalc/
// const env = import.meta.env
// console.log(env)

const characterPath = path.resolve(__dirname, "./imagesrc/characters")
const files = fs.readdirSync(characterPath)

// const specificityPath = path.resolve(__dirname, "./imagesrc/specificity")
// const files_specificity = fs.readdirSync(specificityPath)

const especificityPath = path.resolve(__dirname, "./imagesrc/especificity")
const files_especificity = fs.readdirSync(especificityPath)

// https://vitejs.dev/config/
export default defineConfig(({ command, mode, ssrBuild }) => {
  const temp = [
    {
      source: path.resolve(__dirname, "./imagesrc/adventure/jobs"),
      className: "classchange-icon-[name]",
      excludes: [],
      name: "jobs"
    },
    {
      source: path.resolve(__dirname, "./imagesrc/adventure/sub"),
      className: "character-icon-[name]",
      excludes: [],
      name: "sub"
    },
    {
      source: path.resolve(__dirname, "./imagesrc/common"),
      className: "common-icon-[name]",
      excludes: ["head-2.png"],
      name: "common"
    },
    {
      source: path.resolve(__dirname, "./imagesrc/equipment"),
      className: "equipment-icon-[dirname]-[name]",
      excludes: ["wisdom", "equipmyth"],
      name: "equipment"
    },
    {
      source: path.resolve(__dirname, "./imagesrc/asrahan"),
      className: "asrahan-icon-[name]",
      name: "asrahan"
    },
    // ...files_specificity.map(file => {
    //   const filePath = path.join(specificityPath, file)
    //   return {
    //     source: path.resolve(filePath),
    //     className: (entry: any) => {
    //       return `specificity-icon-${file}-${entry.name.replace(/[().·，：]+/g, "")}`
    //     },
    //     name: file
    //   }
    // }),
    ...files_especificity.map(file => {
      const filePath = path.join(especificityPath, file)
      return {
        source: path.resolve(filePath),
        className: (entry: any) => {
          return `especificity-icon-${file}-${entry.name.replace(/[().·，：]+/g, "")}`
        },
        name: file
      }
    }),
    ...files.map(file => {
      const filePath = path.join(characterPath, file)
      return {
        source: path.resolve(filePath),
        className: (entry: any) => {
          return `character-icon-${file}-${entry.name.replace(/[().·，：]+/g, "")}`
        },
        excludes: ["bg.jpg","material"],
        name: file
      }
    })
  ]

  return {
    mode: process.env.NODE_ENV,
    root: __dirname,
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src")
      }
    },
    define: {
      APP_VERSION: `"${pkg.version}"`
    },
    plugins: [
      unocss({
        rules: [
          [
            /^col-(\d?\d)$/,
            ([, o]) => {
              const span = Number(o)
              const val = `${(span * 100) / 24}%`
              return {
                flex: `0 0 ${val}`
              }
            }
          ]
        ],

        presets: [presetUno()]
      }),
      uncomponents({
        dts: true,
        dirs: ["src/components/"],
        allowOverrides: true,

        directoryAsNamespace: true
      }),
      jsx(),
      vue(),
      createSprite2CssPlugin({
        entries: temp,
        hmr: true,
        target: "/images"
      }),
      viteCompression({
        // threshold: 1024 * 500 // 对大于 1mb 的文件进行压缩
        // verbose: true
        verbose: true,
        disable: false,
        threshold: 10240,
        algorithm: "gzip",
        ext: ".gz"
      })
    ],

    optimizeDeps: {
      exclude: ["electron"]
    },
    build: {
      /* from mode option */
      sourcemap: process.env.NODE_ENV == "development",
      outDir: "../../dist/app/renderer",
      assetsDir: "assets",
      terserOptions: {
        compress: {
          drop_console: true,
          drop_debugger: true
        }
      },
      // rollupOptions: {
      //   output: {
      //     // 重点在这里哦
      //     // entryFileNames: `assets/[name].${timestamp}.js`,
      //     // chunkFileNames: `assets/[name].${timestamp}.js`,
      //     // assetFileNames: `assets/[name].${timestamp}.[ext]`
      //     // entryFileNames: `assets/[name].js`,
      //     // chunkFileNames: `assets/[name].js`,
      //     assetFileNames: `assets/[name].[ext]`
      //   }
      // }
      assetsInlineLimit: 1024 * 30 // 图片转 base64 编码的阈值
    },
    server: {
      host: pkg.env.VITE_DEV_SERVER_HOST,
      port: pkg.env.VITE_DEV_SERVER_PORT
    },
    preview: {
      port: pkg.env.VITE_DEV_SERVER_PORT,
      host: pkg.env.VITE_DEV_SERVER_HOST
    }
  }
})
