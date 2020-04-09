import request from '@/utils/request.js'

export function getCateList(data) {
  return request({
    url: '/api/v1/getCateList',
    method: 'post',
    data
  })
}
