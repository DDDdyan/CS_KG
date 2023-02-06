<template>
  <div class="container">
    <div class="wraper">
      <div class="header">智能问答</div>
      <div class="chatWin">
        <div class="messageBox">
          <div v-for="(item, index) in selectMessageList" :key="index">
            <div v-if="item.send" class="one_message sendMessage">
              <div class="message_wraper">
                <div class="message" v-html="item.message"></div>
                <!-- <div class="img"><img :src="item.imgUrl" alt="" /></div> -->
              </div>
            </div>
            <div v-else class="one_message receiveMessage">
              <div class="message_wraper">
                <!-- <div class="img"><img :src="item.imgUrl" alt="" /></div> -->
                <div class="message" v-html="item.message"></div>
              </div>
            </div>
          </div>
        </div>
        <!-- <div class="InputMess" style="border: 1px solid #ccc"></div> -->
        <div class="InputMess">
          <el-input
            v-model="textarea"
            :rows="2"
            type="textarea"
            placeholder="Please input"
          />
        </div>
        <div class="sendBtn" @click="sendMessage">
          <el-button type="primary">发送</el-button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { getanswer } from "@/api/askquestion";
import { nextTick } from "process";

export default {
  name: "ask",
  data() {
    return {
      selectMessageList: [],
      textarea: "",
    };
  },
  methods: {
    sendMessage() {
      this.selectMessageList.push({
        message: this.textarea,
        send: true,
      });
      getanswer({ question: this.textarea }).then((res) => {
        console.log("答案", res);
        if (res.code == 20000) {
          this.selectMessageList.push({
            message: res.data,
            send: false,
          });
          nextTick(()=>{
            document.querySelector('.messageBox').scrollTop  += 999999

          })
        }
      });
      this.textarea = "";
    },
  },
};
</script>
<style lang="scss" scoped>
.container {
  width: 100%;
  height: 100%;
  margin-top: 50px;
  display: flex;
  justify-content: center;
}
.wraper {
  width: 600px;
  height: 600px;
  box-shadow: 0px 0px 10px 0px rgb(14 14 14 / 15%);
  border-radius: 9px;
  overflow: hidden;
  .header {
    width: 100%;
    height: 80px;
    background-color: #1b53d0;
    color: #fff;
    padding-left: 20px;
    font-size: 18px;
    line-height: 80px;
    font-weight: bold;
  }
  .chatWin {
    width: 100%;
    background: #fff;
    position: relative;
    height: calc(100% - 80px);
    
    .messageBox {
      width: 100%;
      height: calc(100% - 100px);
      padding: 5px 5px 0px 5px;
      overflow-y: scroll;
      box-sizing: border-box;
      
      .one_message {
        .message_wraper {
          display: flex;
          align-items: center;
          justify-content: flex-end;

          margin-bottom: 15px;
        }
        .message {
          border-radius: 25px;
          padding: 5px 10px;
          background: #1b53d0;
          max-width: 80%;
          //   word-break: break-all;
          color: #fff;
        }
      }
      .sendMessage {
        justify-content: flex-end !important;
      }
      .receiveMessage {
        justify-content: flex-start !important;
        .message_wraper {
          justify-content: flex-start !important;
        }
        .message {
          border-radius: 25px;
          padding: 5px 10px;
          background: #c8c9cc;
          max-width: 80%;
        }
      }
    }
    .messageBox::-webkit-scrollbar {
      display: none;
    }
    .InputMess {
      width: 100%;
      position: absolute;
      bottom: 0;
      height: 100px;

      ::v-deep .el-textarea {
        width: 100%;
        height: 100px;
        border: none;
        .el-textarea__inner {
          height: 100% !important;
        }
        .el-textarea__inner:focus {
          outline: 0;
          border-color: #ccc;
        }
      }
    }
    .InputMess::-webkit-scrollbar {
      display: none !important;
    }
    .sendBtn {
      position: absolute;
      bottom: 0;
      right: 0;
    }
  }
}
</style>
