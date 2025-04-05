import { defineConfig } from 'unocss'
// import { presetAttributify } from 'unocss'
import { blackA, green } from '@radix-ui/colors'

export default defineConfig({
  // presets: [presetAttributify()],
  rules:[
    [
      "cursor-pointer",
      {
        cursor: "var(--cursor-pointer)",
      },
    ]
  ],
  theme: {
    colors: {},
  },
})
