import Vue from 'vue'
import VueRouter from 'vue-router'

/* Layout */
import Layout from '@/layout'

Vue.use(VueRouter)
// 基础路由
const constantRoutes = [
  {
    path: '/',
    name: 'HomePage',
    component: Layout,
    redirect: '/index',
    children: [
      {
        path: 'index',
        component: () => import('@/views/index')
      }
    ]
  },
  {
    path: '/login',
    name: 'LoginPage',
    meta: {
      title: '登录页'
    },
    component: () => import('@/views/login'),
  },
  {
    path: '/site',
    name: 'SitePage',
    component: Layout,
    redirect: '/site/index',
    children: [
      {
        path: 'index',
        component: () => import('@/views/site')
      },
      {
        path: 'emial',
        component: () => import('@/views/site/emial')
      },
      {
        path: 'expand',
        component: () => import('@/views/site/expand')
      },
    ]
  },
  {
    path: '/user',
    name: 'UserPage',
    component: Layout,
    redirect: '/user/index',
    children: [
      {
        path: 'index',
        meta: {
          title: '网站用户'
         },
        component: () => import('@/views/user')
      },
      {
        path: 'admin',
        meta: {
          title: '管理员'
         },
        component: () => import('@/views/user/admin')
      },
      {
        path: 'role',
        meta: {
          title: '用户角色'
         },
        component: () => import('@/views/user/role')
      },
    ]
  },
  {
    path: '/cate',
    name: 'catePage',
    component: Layout,
    redirect: '/cate/index',
    children: [
      {
        path: 'index',
        meta: {
          title: '分类管理'
         },
        component: () => import('@/views/cate')
      },
    ]
  },
  {
    path: '/tag',
    name: 'tagPage',
    component: Layout,
    redirect: '/tag/index',
    children: [
      {
        path: 'index',
        meta: {
          title: '标签管理'
         },
        component: () => import('@/views/tag')
      },
    ]
  },
  {
    path: '/article',
    name: 'articlePage',
    component: Layout,
    redirect: '/article/index',
    children: [
      {
        path: 'index',
        meta: {
          title: '文章管理'
         },
        component: () => import('@/views/article')
      },
      {
        path: 'add',
        meta: {
          title: '文章发布'
         },
        component: () => import('@/views/article/add')
      },
    ]
  },
  {
    path: '/backUp',
    name: 'backUp',
    component: Layout,
    redirect: '/backUp/index',
    children: [
      {
        path: 'index',
        meta: {
          title: '备份管理'
         },
        component: () => import('@/views/backUp')
      },
    ]
  },
]

// const router = new VueRouter({
//   mode: 'history',
//   base: process.env.BASE_URL,
//   scrollBehavior: () => ({ y: 0 }),
//   routes
// })

// export default router

const createRouter = () => new VueRouter({
  mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465 -- 重置路由
export function resetRouter () {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
