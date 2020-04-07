import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import './assets/css/reset.css'
import './assets/css/custom.scss'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import mixin from './mixin'

if (process.env.NODE_ENV !== 'production') require('./mockjs/index.js')

Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.mixin(mixin)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
