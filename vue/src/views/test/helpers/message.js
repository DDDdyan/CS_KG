import { fakeMessages } from './fake-messages' //这个也是一个js 是机器的自定义一些回答消息的需要新建文件

export const messageService = {
  createMessage
}

function createMessage () {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      let randomNumber = Math.floor(Math.random() * fakeMessages.length)
      resolve(fakeMessages[randomNumber])
    }, 1000)
  })
}

