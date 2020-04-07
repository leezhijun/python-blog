import axios from 'axios'
import { Message } from 'element-ui'
import { getToken } from './auth.js'

const baseUrl = 'http://localhost:8081/'

// 创建axios实例
const service = axios.create({
  baseURL: baseUrl, // api的baseUrl
  timeout: 5000, // 请求超时
  headers: { 'Content-Type': 'application/json' },
})

// 请求前拦截
service.interceptors.request.use(config => {
  config.headers['authToken'] = getToken()
  return config
},err => {
  console.log(err)
  Promise.reject(err)
})

// 接受数据拦截
service.interceptors.response.use(
  response => { // 请求有响应
    const res = response.data
    console.log('response---',response)
    if (res.code===0) { // 数据返回正常
      return res
    } else { // 数据返回不正常
      if (res.code===100) { // 没有登陆，或者登陆失效
        Message({
          message: '登陆失效，请重新登陆后操作!',
          type: 'error',
          duration: 3 * 1000,
          onClose: ()=>{
            location.href = '/login'
          }
        })
      }
      return Promise.reject(res)
    }
  },error => { // 请求无响应报错
    console.log('response-err',error)
    Message({
      message: error.message,
      type: 'error',
      duration: 3 * 1000,
    })
    return Promise.reject(error)
  })

  export default service
