import request from '@/utils/request.js'

export function getArticleList(data) {
  return request({
    url: '/articleSelect',
    method: 'post',
    data
  })
}

export function addArticle(data) {
  return request({
    url: '/addArticle',
    method: 'post',
    data
  })
}

export function articleDelete(data) {
  return request({
    url: '/articleDelete',
    method: 'post',
    data
  })
}

export function articleUpdate(data) {
  return request({
    url: '/articleUpdate',
    method: 'post',
    data
  })
}

export function articleSelectId(data) {
  return request({
    url: '/articleSelectId',
    method: 'post',
    data
  })
}
