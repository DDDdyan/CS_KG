<template>
  <el-container>
    <el-header style="text-align: left; font-size: 30px">
      <el-dropdown>
        <el-title type="text" style="margin-top: 30px;width: 1200px; size: auto"> 学情反馈</el-title>
        <el-button type="text" style="margin-top: 30px;width: 150px; size: auto" @click="dialogTableVisible = true"> 学习推荐</el-button>
        <el-dialog title="参考" :visible.sync="dialogTableVisible">
          <el-table :data="gridData">
            <el-table-column property="date" label="相似学生" width="150"></el-table-column>
            <el-table-column property="name" label="下一步学习推荐" width="200"></el-table-column>
            <el-table-column property="address" label="难易度"></el-table-column>
          </el-table>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="dialogTableVisible = false">确 定</el-button>
          </div>
        </el-dialog>

      </el-dropdown>
      <span> <VueBotUI
          :messages = "messageData"
          :options = "botOptions"
          :bot-typing="botTyping"
          :input-disable="inputDisable"
          :is-open="false"
          @msg-send = "messageSendHandler"
          @init="botStart"
      /></span>
    </el-header>
  <el-main>
    <el-table :data="tableData"><!--:data 绑定data()的数组值,会动态根据其变化而变化-->
      <el-table-column prop="id" label="序号" />
      <!--:data prop绑定{}中的key，label为自定义显示的列表头-->
      <el-table-column prop="title" label="知识点名称" />
      <el-table-column prop="desc" label="累计查看次数" show-overflow-tooltip />
      <!--对于描述可能很长的情况，做个省略的显示的优化功能，使用element ui属性 show-overflow-tooltip-->
      <el-table-column :formatter="formatDate" prop="update" label="最新操作时间"/>
      <el-table-column prop="update" label="操作">

        <!--在修改操作的时候是对本行进行操作的，要想获取本行的数据，并透传给调用方法，需要使用vue里一个叫插件槽的东西
        基本语法：<template slot-scope="scope"></template>-->
        <template slot-scope="scope">
          <!--表格控件中增加一列，列里增加一个编辑按钮，使用组件 Link 文字链接，并带个icon
          基本语法：<el-link icon="el-icon-edit"></el-link>-->
          <el-link icon="el-icon-edit" @click="dialogProductUpdate(scope.row)"> 备注 </el-link>

        </template>
      </el-table-column>
    </el-table>
    <div class="pagination">
        <el-pagination
          :current-page.sync="currentPage"
          :page-size="10"
          layout="total, prev, pager, next, jumper"
          :total="totalCount"
          @current-change="handleCurrentChange"
        >
        </el-pagination>
    </div>
  </el-main>
  
  </el-container>

</template>>
<script>
import * as echarts from 'echarts'
import { apiProductList, apiProductCreate, apiProductUpdate } from '@/api/product'
import { apiProductDelete, apiProductRemove, apiProductSearch } from '@/api/product'
import store from '@/store'
import moment from 'moment'
import  { VueBotUI } from 'vue-bot-ui'
import { messageService } from './helpers/message' //需要你新建js文件
export default {
  name: "Contactus",
  components:{
    VueBotUI
  },
  data() {
    return {
      gridData: [{
        date: '036',
        name: '程序表示',
        address: '易'
      }, {
        date: '031',
        name: '静态分析与bug检查',
        address: '中'
      }, {
        date: '152',
        name: '流敏感分析',
        address: '难'
      }],
      dialogTableVisible: false,




      tableData: [],
      // 获得登录的名字
      op_user: store.getters.name,
      // 定义产品参数
      product: {
        id: undefined,
        title: undefined,
        keyCode: undefined,
        desc: undefined,
        operator: this.op_user
      },

      //以下是插件data
      botTyping:true,
      messageData: [],
      inputDisable:false,
      botOptions : {
        botTitle: '智能问答', //显示是什么
        botAvatarImg:'http://placehold.it/200x200',
        botAvatarSize:'32', //这个是头像的大小
        animation:true,
        messages:[
          {
            agent: 'bot', // Required. 'bot' or 'user'
            type: 'text', // Required. Bubble message component type: 'text' / 'button'
            text: 'Hello. How can I help you', // Required. The message
            disableInput: false, // Disable message input or not
          },
          {
            agent: 'user',
            type: 'text', // always
            text: 'I need a new laptop',
          },
        ]
        // 请参阅下面的选项列表

      },
      currentPage:1,
      totalCount:0

    };
  },
  // 页面生命周期中的创建阶段调用
  created() {
    // 调用methods的方法，即初次加载就请求数据
    this.getProductList(this.currentPage)
  },

  methods: {



    // getProductList自定义方法名，提供其他地方调用this.getProductList
    getProductList(page) {
      // 固定格式调用api配置方法，并将返回结果回调给response
      apiProductList(page).then(response => {
        // console.log（）是调试打印，可以在chrome开发者工具中查看
        console.log(response.data)
        // 将返回的结果赋值给变量 tableData
        this.tableData = response.data
        this.totalCount = response.total
      })
    },
    dialogProduct() { // 其他变量的引用需要通过this.来给定
      // 添加先初始化空状态
      this.product.id = undefined
      this.product.keyCode = ''
      this.product.title = ''
      this.product.desc = ''
      this.product.operator = this.op_user

      // 弹出对话框设置为true
      this.dialogProductShow = true
    },
    pCreate() {
      // 请求API进行添加
      apiProductCreate(this.product).then(response => {
        // 如果request.js没有拦截即表示成功，给出对应提示和操作
        this.$notify({
          title: '成功',
          message: '项目或产品添加成功',
          type: 'success'
        })
        // 关闭对话框
        this.dialogProductShow = false
        // 重新查询刷新数据显示
        this.getProductList()
      })
    },
    // 获取当前编辑行数数据并赋值给product
    dialogProductUpdate(row) {
      // 添加先初始化空状态
      this.product.id = row.id
      this.product.keyCode = row.keyCode
      this.product.title = row.title
      this.product.desc = row.desc
      this.product.operator = this.op_user

      // 标记弹窗是修改操作
      this.dialogProductStatus = 'UPDATE'
      // 弹出对话框设置为true
      this.dialogProductShow = true
    },
    pUpdate() {
      apiProductUpdate(this.product).then(res => {
        this.$notify({
          title: '成功',
          message: '项目或产品修改成功',
          type: 'success'
        })
        // 关闭对话框
        this.dialogProductShow = false
        // 重新查询刷新数据显示
        this.getProductList()
      })
    },
    pHardRemove(id) {
      // 在这里的删除逻辑里一般要给个二次确认是否进行操作，使用的是组件 MessageBox 弹框中确认消息 功能是提示用户确认其已经触发的动作，并询问是否进行此操作，确认继续执行或者取消此操作，调用的是$confirm对应可设置type字段表明消息类型，可以为 success，error，info 和 warning 更多定制属性可直接参考官方
      // 对应的参数是 (提示内容，标题 {自定义确定按钮文案，自定义取消按钮文案, 对话框类型}
      this.$confirm('此操作为硬删除将永久删除该项目, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
        // then 点击confirmButton后执行的方法，否则是不执行关闭对话框
      }).then(() => {
        // vue click时候传d的id需要定义参数
        apiProductDelete(id).then(res => {
          this.$message({
            type: 'success',
            message: '删除成功!'
          })
          // 重新查询刷新数据显示
          this.getProductList()
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    pSoftRemove(id) {
      this.$confirm('此操作将停用该数据不显示但会在数据库中进行保留, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        apiProductRemove(id).then(res => {
          this.$message({
            type: 'success',
            message: '删除成功!'
          })
          // 重新查询刷新数据显示
          this.getProductList()
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    // 条件搜索功能
    searchProduct() {
      apiProductSearch(this.search).then(res => {
        this.tableData = res.data
      })
    },
    formatDate(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      // 使用moment格式化时间，由于我的数据库是默认时区，偏移量设置0，各自根据情况进行配置
      return moment(date).utcOffset(0).format('YYYY-MM-DD HH:mm')
    },


    //以下是插件内容
    botStart () {   //初始化 会发送什么
      this.botTyping = true
      setTimeout(() => {
        this.botTyping = false
        this.messageData.push({
          agent : 'bot' ,
          type : 'button' ,
          text : 'Hello. How can I help you' ,
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
    },
    handleCurrentChange(page){
      console.log(page)
      this.getProductList(page)
    }
  }
}


</script>

