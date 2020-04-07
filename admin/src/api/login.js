import request from '@/utils/request.js'

export function login(data) {
  return request({
    url: '/api/v1/login',
    method: 'post',
    data
  })
}
