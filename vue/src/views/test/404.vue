<VueBotUI
    :messages = "messageData"
    :options = "botOptions"
    :bot-typing="botTyping"
    :input-disable="inputDisable"
    :is-open="false"
    @msg-send = "messageSendHandler"
    @init="botStart"
/>
<script >
import  { VueBotUI } from 'vue-bot-ui'
import { messageService } from './helpers/message' //需要你新建js文件
export default {
  name: "Contactus",
  components:{
    VueBotUI
  },
  data() {
    return {
      botTyping:true,
      messageData: [],
      inputDisable:false,
      botOptions : {
        botTitle: '小康客服', //显示是什么
        botAvatarImg:'机器人头像 你可以自定义',
        botAvatarSize:'32', //这个是头像的大小
        animation:true
        // 请参阅下面的选项列表
      },
    };
  },
  methods: {
    botStart () {   //初始化 会发送什么
      this.botTyping = true
      setTimeout(() => {
        this.botTyping = false
        this.messageData.push({
          agent : 'bot' ,
          type : 'button' ,
          text : '欢迎您！使用小康智能客服,请问有什么需要吗？？' ,
        })
      }, 1000)
    },
    messageSendHandler(value){  //点击发送传一个值
      this.messageData.push({
        agent: 'user',
        type: 'text',
        text: value.text
      })
      this.getResponse()   //调用下面机器人自定义的消息
      console.log("点击发送了")
    },
    getResponse () {
      this.botTyping = true
      messageService.createMessage()
          .then((response) => {
            const replyMessage = {
              agent: 'bot',
              ...response
            }

            this.inputDisable = response.disableInput
            this.messageData.push(replyMessage)

            // finish
            this.botTyping = false
          })
    }
  }
}


</script>

