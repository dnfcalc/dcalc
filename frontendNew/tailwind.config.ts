import type { Config } from 'tailwindcss'

export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
    './node_modules/shadcn-vue/lib/**/*.{js,ts,vue}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
} satisfies Config
