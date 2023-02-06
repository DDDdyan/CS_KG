import request from '@/utils/request'


export function apiProductList(page) {
  return request({
    url: `/api/product/list?page=${page}`,
    method: 'get'
  })
}

export function apiAddProduct(requestBody) {
  return request({
    url: '/api/product/create',
    method: 'post',
    data: requestBody
  })
}

// 条件查询
export function apiProductSearch(params) {
  return request({
    url: '/api/product/search',
    method: 'get',
    params: params
    // params定义的是个josn直接传过来就行，可以不用二次封装，上层传过来的格式如：{"title":"value", "keyCode":"value"}
  })
}

// 调用项目增加接口
export function apiProductCreate(requestBody) {
  return request({
    url: '/api/product/create',
    method: 'post',
    data: requestBody
  })
}

// 调用更新项目接口
export function apiProductUpdate(requestBody) {
  return request({
    url: '/api/product/update',
    method: 'post',
    data: requestBody
  })
}

// 调用真实删除数据库接口
export function apiProductDelete(id) {
  return request({
    url: '/api/product/delete',
    method: 'delete',
    params: {
      'id': id
    }
  })
}

// 软删除，更改数据状态
export function apiProductRemove(id) {
  return request({
    url: '/api/product/remove',
    method: 'post',
    params: {
      'id': id
    }
  })
}

