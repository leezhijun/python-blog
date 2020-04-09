import request from '@/utils/request.js'

export function getSiteExpandList(data) {
  return request({
    url: '/api/v1/getSiteExpandList',
    method: 'post',
    data
  })
}
