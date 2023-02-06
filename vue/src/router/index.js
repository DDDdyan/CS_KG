import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Layout from '@/layout'


export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },
  
  {
    path: '/',
    component: Layout,
    redirect: '/2dViewby',
    children: [{
      path: '/2dViewby',
      name: '2dViewby',
      component: () => import('@/views/2dViewby'),
      meta: { title: '编译原理KG', icon: 'example' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/2dView',
    children: [{
      path: '/2dView',
      name: '2dView',
      component: () => import('@/views/2dView'),
      meta: { title: '安全编程语言设计KG', icon: 'example' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/ArticleEditor',
    children: [{
      path: '/ArticleEditor',
      name: 'ArticleEditor',
      component: () => import('@/views/ArticleEditor'),
      meta: { title: '新增节点编辑', icon: 'form' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/Contactusr',
    children: [{
      path: '/Contactus',
      name: 'Contactus',
      component: () => import('@/views/test/Contactus'),
      meta: { title: '问答&推荐', icon: 'form' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/askquestion',
    children: [{
      path: '/askquestion',
      name: 'askquestion',
      component: () => import('@/views/AskQuestion.vue'),
      meta: { title: '问答', icon: 'form' }
    }]
  },

  {
    path: '/demo',
    component: Layout,
    redirect: '/demo',
    meta: { title: 'else', icon: '设置' },
    children: [{
      path: 'upload',
      name: 'Upload',
      component: () => import('@/views/demo/uploadDemo'),
      meta: { title: '文件上传Demo' }
    },
    {
      path: 'chart',
      name: 'chart',
      component: () => import('@/views/demo/echartsDemo'),
      meta: { title: 'Echarts Demo' }
    }]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
