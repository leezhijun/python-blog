import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

/* Layout */
import Layout from '@/layout'

Vue.use(VueRouter)

const constantRoutes = [
  {
    path: '/',
    name: 'Home',
    component: Layout
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

// const router = new VueRouter({
//   mode: 'history',
//   base: process.env.BASE_URL,
//   scrollBehavior: () => ({ y: 0 }),
//   routes
// })

// export default router

const createRouter = () => new VueRouter({
  // mode: 'history', // require service support
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
