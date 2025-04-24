import type { AxiosInstance, AxiosResponse } from 'axios'
import axios from 'axios'
import { h } from 'vue'
import { gzip, ungzip } from 'pako'
import { useInfoStore } from '@/stores'
import { useDialog } from '@/components/hooks/dialog'
// import { useAppStore, useConfigStore } from '@/store'
// import { useDialog } from '@/components/hooks/dialog'

export interface HttpResponse<T = unknown> extends AxiosResponse {
  code?: number
  message: string
  data: T
  state?: number
}

let instance: AxiosInstance | null = null

let baseURL = '/api'

// 避免远程开发的时候冲突
if (process.env.NODE_ENV == 'development') {
  baseURL = 'http://127.0.0.1:47173/api'
}

if (import.meta.env.MODE == 'web' || import.meta.env.MODE == 'show') {
  baseURL = 'https://api.dnftools.com/'
}

if(import.meta.env.MODE == 'test') {
  baseURL = 'https://testapi.dnftools.com/'
}

// 解压
function unzip(key: string) {
  // 将二进制字符串转换为字符数组

  const charData = key.split('').map((x) => {
    return x?.charCodeAt(0)
  })

  // 将数字数组转换成字节数组
  const binData = new Uint8Array(charData)

  // 解压
  const data = ungzip(binData)

  const decoder = new TextDecoder()
  const str = decoder.decode(data)

  // unescape(str)  --->解压后解码，防止中午乱码
  return str
}

export function defineRequest<T>(fn: (ax: AxiosInstance) => T) {
  if (!instance) {
    instance = axios.create({
      baseURL,
    })

    instance.interceptors.request.use(
      (request) => {
        // const configStore = useConfigStore()
        // const token = configStore.token
        // const uid = useAppStore().uid

        const token = useInfoStore().alter_token

        if (token) {
          request.headers['Alter-Token'] = token
        }

        return request
      },
      (error) => {
        // do something
        return Promise.reject(error)
      },
    )

    instance.defaults.headers.post['Content-Type'] = 'application/json;charset=UTF-8'
    // instance.defaults.headers["Accept-Encoding"] = "gzip"
    // instance.defaults.headers["Content-Encoding"] = "gzip"
    // add response interceptors
    instance.interceptors.response.use(
      async (response: AxiosResponse<HttpResponse>) => {
        if (response.data.code === 500) {
          const { alert } = useDialog()
          await alert({
            content: () => {
              return h(
                'div',
                {
                  class: 'justify-center text-hex-d4d6b6 text-center',
                  style: 'white-space:pre-wrap;width:250px;margin:10px',
                },
                `出现错误，可加群反馈:183439472\n${response.data.message}`,
              )
            },
          })
        }
        // 解密数据
        if (typeof response.data.data == 'string') {
          try {
            const data = unzip(atob(response.data.data as string))
            response.data.data = JSON.parse(data)
          } catch (e) {}
        }
        return response.data
      },
      async (error: Error) => {
        return Promise.reject(error)
      },
    )
  }

  return fn(Object.create(instance))
}
