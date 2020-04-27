import request from '@/utils/request.js'
// 登陆
export function login(data) {
  return request({
    url: '/login',
    method: 'post',
    data
  })
}
// 退出
export function loginOut() {
  return request({
    url: '/loginOut',
    method: 'post',
  })
}
