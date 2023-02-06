import request from '@/utils/request'

export function apiClicksList() {
  return request({
    url: '/api/clicks/list',
    method: 'get'
  })
}

// 条件查询
export function apiClicksSearch(params) {
  return request({
    url: '/api/clicks/search',
    method: 'get',
    params: params
    // params定义的是个josn直接传过来就行，可以不用二次封装，上层传过来的格式如：{"title":"value", "keyCode":"value"}
  })
}

// 调用项目增加接口
export function apiClicksCreate(requestBody) {
  return request({
    url: '/api/clicks/create',
    method: 'post',
    data: requestBody
  })
}

// 调用更新项目接口
export function apiClicksUpdate(requestBody) {
  return request({
    url: '/api/clicks/update',
    method: 'post',
    data: requestBody
  })
}

// 调用真实删除数据库接口
export function apiClicksDelete(id) {
  return request({
    url: '/api/clicks/delete',
    method: 'delete',
    params: {
      'id': id
    }
  })
}

// 软删除，更改数据状态
export function apiClicksRemove(id) {
  return request({
    url: '/api/clicks/remove',
    method: 'post',
    params: {
      'id': id
    }
  })
}

