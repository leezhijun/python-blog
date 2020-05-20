// 获取token
export const getToken = () => {
  return sessionStorage['Token'] ? sessionStorage['Token'] : ''
}

// 存储token
export const saveToken = (token) => {
  sessionStorage['Token'] = token
}

// 清除token
export const clearToken = (token) => {
  sessionStorage.removeItem('Token')
}
