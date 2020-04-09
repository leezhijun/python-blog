import request from '@/utils/request.js'

export function getUserList(data) {
  return request({
    url: '/api/v1/getUserList',
    method: 'post',
    data
  })
}
