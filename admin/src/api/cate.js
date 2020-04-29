import request from '@/utils/request.js'

export function getCateList(data) {
  return request({
    url: '/cateSelect',
    method: 'post',
    data
  })
}

export function addCate(data) {
  return request({
    url: '/addCate',
    method: 'post',
    data
  })
}

export function cateDelete(data) {
  return request({
    url: '/cateDelete',
    method: 'post',
    data
  })
}

export function cateUpdateShow(data) {
  return request({
    url: '/cateUpdateShow',
    method: 'post',
    data
  })
}

export function cateUpdate(data) {
  return request({
    url: '/cateUpdate',
    method: 'post',
    data
  })
}

export function cateOneAll(data) {
  return request({
    url: '/cateOneAll',
    method: 'post',
    data
  })
}
