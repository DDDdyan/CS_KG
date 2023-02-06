import request from '@/utils/request'



export function apiAppsSearch(requestBody) {
  return request({
    url: '/api/application/search',
    method: 'post',
    data: requestBody
  })
}

// 产品选择项目列表
export function apiAppsProduct() {
  return request({
    url: '/api/application/product',
    method: 'get'
  })
}

// 调用应用增加/修改统一接口
export function apiAppsCommit(requestBody) {
  return request({
    url: '/api/application/update',
    method: 'post',
    data: requestBody
  })
}

// 获取应用列表，可按照appid 或者 note模糊查询
export function apiAppsIds(value) {
  return request({
    url: '/api/application/options?value=' + value,
    method: 'get'
  })
}

// 获取文章列表
export function getArticleList(val) {
  return request({
    url: 'api/markdown/getArticle?name=' + val,
    method: 'get'
  })
}
// 更新文章内容
export function updateArticle(requestBody) {
  return request({
    url: '/api/markdown/update',
    method: 'post',
    data: requestBody
  })
}
