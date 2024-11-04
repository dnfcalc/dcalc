import { builtinModules } from "node:module"
import { defineConfig } from "vite"
import pkg from "../../package.json"

export default defineConfig({
  root: __dirname,
  build: {
    outDir: "../../dist/app/preload",
    lib: {
      entry: "index.ts",
      formats: ["cjs"],
      fileName: () => "[name].cjs"
    },
    /* from mode option */
    sourcemap: process.env.NODE_ENV == "development",
    /* from mode option */
    minify: process.env.NODE_ENV === "production",
    // emptyOutDir: true,
    rollupOptions: {
      external: ["electron", ...builtinModules,
        ...builtinModules.map((m) => `node:${m}`),
        ...Object.keys(pkg.devDependencies || {})]
    }
  }
})
