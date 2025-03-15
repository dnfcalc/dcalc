let baseURL = 'https://image.dnftools.com'

// 避免远程开发的时候冲突
if (process.env.NODE_ENV == 'development') {
  baseURL = 'http://127.0.0.1:3000'
}

if (import.meta.env.MODE == 'web' || import.meta.env.MODE == 'show') {
  baseURL = 'https://image.dnftools.com'
}

export const getImageURL = (image: string) => {
  image = image.startsWith('/') ? image : `/${image}`
  return `${baseURL}${image}`
}

export const getLocalImageURL = (url:string)=>{
  return new URL(url, import.meta.url).href
}
