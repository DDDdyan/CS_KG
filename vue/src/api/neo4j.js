import request from '@/utils/request'

export function getAllData(name,num) {
  return request({
    // url: '/vue-admin-template/user/login',
    url: '/api/neo4j/getAllData',
    method: 'get',
    params:{name,num}
  })
}

export function addNode(data) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/api/neo4j/addnode',
    method: 'post',
    data:data
  })
}

export function deleteNode(id) {
  return request({
    url: '/api/neo4j/deletenode',
    method: 'get',
    params:{id}
  })
}
