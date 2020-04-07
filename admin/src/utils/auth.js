// 获取token
export const getToken = () => {
  return sessionStorage['Token'] ? sessionStorage['Token'] : ''
}

// 存储token
export const saveToken = (token) => {
  sessionStorage['Token'] = token
}
