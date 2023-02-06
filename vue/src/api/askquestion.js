import request from '@/utils/request'

export function getanswer(data) {
  return request({
    url: '/api/askquestion/getanswer',
    method: 'post',
    data
  })
}


