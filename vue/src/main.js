import Vue from 'vue'
import 'normalize.css/normalize.css' // A modern alternative to CSS resets

// import locale from 'element-ui/lib/locale/lang/en' // lang i18n

import '@/styles/index.scss' // global css

import App from './App'
import store from './store'
import router from './router'

import '@/icons' // icon
import '@/permission' // permission control

// import 'jquery/dist/jquery.min'
// import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap'
import $ from 'jquery' //上述两行引入之后整体样式出现了问题？？？？？？？？

import mavonEditor from 'mavon-editor' // 全局注册,并且导入mavon-editor样式
import 'mavon-editor/dist/css/index.css' // 全局注册,并且导入mavon-editor样式
import VueTreeList from 'vue-tree-list'
Vue.use(VueTreeList)
Vue.use(mavonEditor)
new Vue({
  'el': '#main',
  data() {
    return { value: '' }
  }
})
/**
 * If you don't want to use mock-server
 * you want to use MockJs for mock api
 * you can execute: mockXHR()
 *
 * Currently MockJs will be used in the production environment,
 * please remove it before going online ! ! !
 */
if (process.env.NODE_ENV === 'production') {
  const { mockXHR } = require('../mock')
  mockXHR()
}

// set ElementUI lang to EN
// Vue.use(ElementUI, { locale })
// 如果想要中文版 element-ui，按如下方式声明
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
