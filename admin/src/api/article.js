import request from '@/utils/request.js'

export function getArticleList(data) {
  return request({
    url: '/api/v1/getArticleList',
    method: 'post',
    data
  })
}
