import Mock from 'mockjs'

// 正常登陆
Mock.mock('http://localhost:8081/mockApi/v1/login',{
  code: 0,
  data: {
    username: 'test',
    age: '18',
    sex: '男'
  }
})

// 登陆报错
// Mock.mock('http://localhost:8081/mockApi/v1/login',{
//   code: 100,
//   data: {},
//   message: '登陆失效'
// })

Mock.mock('http://localhost:8081/mockApi/v1/getSiteExpandList',{
  code: 0,
  data: {
    data: [
      {
        key: 'timeche',
        des: '缓存时间',
        val: '10'
      },
      {
        key: 'maxUpload',
        des: '最大上传',
        val: '100000'
      },
      {
        key: 'uploadFile',
        des: '上传文件类型',
        val: 'png|gif|jpg|jpeg|zip|rar'
      },
    ],
    total: 3
  }
})

Mock.mock('http://localhost:8081/mockApi/v1/getUserList',{
  code: 0,
  data: {
    data: [
      {
        id: '1',
        name: '11111',
        six: '男',
        email: '123@qq.com',
        phone: '13320031323',
        ip: '192.168.35.89',
        time: '2010-10-10'
      },
      {
        id: '2',
        name: '222222',
        six: '男',
        email: '123@qq.com',
        phone: '13320031323',
        ip: '192.168.35.89',
        time: '2010-10-10'
      },
      {
        id: '3',
        name: '333333',
        six: '女',
        email: '123@qq.com',
        phone: '13320031323',
        ip: '192.168.35.89',
        time: '2010-10-10'
      },
    ],
    total: 3
  }
})

Mock.mock('http://localhost:8081/mockApi/v1/getCateList',{
  code: 0,
  data: {
    data: [
      {
        id: '1',
        name: '11111',
        nickname: 'nickname'
      },
      {
        id: '2',
        name: '11111',
        nickname: 'nickname'
      },
      {
        id: '3',
        name: '11111',
        nickname: 'nickname'
      },
    ],
    total: 3
  }
})

Mock.mock('http://localhost:8081/mockApi/v1/getArticleList',{
  code: 0,
  data: {
    data: [
      {
        id: '1',
        title: '11111',
        status: '发布'
      },
      {
        id: '1',
        title: '11111',
        status: '草稿'
      },
      {
        id: '3',
        title: '11111',
        status: '草稿'
      },
    ],
    total: 3
  }
})
