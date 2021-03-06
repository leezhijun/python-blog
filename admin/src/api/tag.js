import request from '@/utils/request.js'

export function getTagList(data) {
  return request({
    url: '/tagSelect',
    method: 'post',
    data
  })
}

export function addTag(data) {
  return request({
    url: '/addTag',
    method: 'post',
    data
  })
}

export function tagDelete(data) {
  return request({
    url: '/tagDelete',
    method: 'post',
    data
  })
}

export function tagUpdate(data) {
  return request({
    url: '/tagUpdate',
    method: 'post',
    data
  })
}

export function searchTag(data) {
  return request({
    url: '/tagSearchName',
    method: 'post',
    data
  })
}

export function delTagArticle(data) {
  return request({
    url: '/tagArticleDelete',
    method: 'post',
    data
  })
}
