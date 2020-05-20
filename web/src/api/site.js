import request from '@/utils/request.js'

export function getSiteExpandList(data) {
  return request({
    url: '/siteIndex',
    method: 'post',
    data
  })
}

export function updateSiteIndex(data) {
  return request({
    url: '/updateSiteIndex',
    method: 'post',
    data
  })
}
