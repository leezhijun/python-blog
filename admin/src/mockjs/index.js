import Mock from 'mockjs'

// 正常登陆
Mock.mock('http://localhost:8081/api/v1/login',{
  code: 0,
  data: {
    username: 'test',
    age: '18',
    sex: '男'
  }
})

// 登陆报错
// Mock.mock('http://localhost:8081/api/v1/login',{
//   code: 100,
//   data: {},
//   message: '登陆失效'
// })
