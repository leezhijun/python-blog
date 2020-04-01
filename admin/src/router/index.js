import Vue from 'vue'
import VueRouter from 'vue-router'

/* Layout */
import Layout from '@/layout'

Vue.use(VueRouter)

const constantRoutes = [
  {
    path: '/',
    name: 'Home',
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
    path: '/user',
    name: 'Home',
    component: Layout,
    redirect: '/user/index',
    children: [
      {
        path: 'index',
        component: () => import('@/views/user')
      },
      {
        path: 'add',
        component: () => import('@/views/user/add')
      }
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
