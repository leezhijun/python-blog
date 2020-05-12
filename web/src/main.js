import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import mixin from './mixin';
import './assets/css/reset.css'
import './assets/css/custom.scss'
import VueAwesomeSwiper from 'vue-awesome-swiper'
// import style
import 'swiper/css/swiper.css'
Vue.config.productionTip = false
Vue.mixin(mixin);
Vue.use(VueAwesomeSwiper, /* { default options with global component } */)
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
