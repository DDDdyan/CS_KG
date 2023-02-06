<template>
  <div>
    <el-input
      v-model="article.title"
      style="margin: 10px 0px;font-size: 18px;"
      placeholder="请输入知识名称"
    ></el-input>
    <mavon-editor
      v-model="article.articleContentMd"
      style="height: 100%;"
      ref="md"
      @save="saveArticles"
      fontSize="16px"
      @imgAdd="handleEditorImgAdd"
    >
    </mavon-editor>
  </div>
</template>

<script>
import request from '@/utils/request'
export default {
  name: 'Editor',
  data() {
    return {
      article: {
        id: '',
        title: '',
        html: '',
        md: ''
      }
    }
  },
  methods: {
    saveArticles(value, render) {
      if (this.article.title && value) {
        request({
          url: '/api/markdown/save',
          method: 'post',
          data: {
            id: this.guid(),
            title: this.article.title,
            md: value,
            html: render
          }
        }).then(val => {
          console.log(val)
          this.$message({
            type: 'info',
            message: '保存成功'
          })
        })
      } else {
        this.$message.error('标题不能为空或内容不能为空')
      }
      // value 是 md，render 是 html

      // this.$confirm('是否保存并发布文章?', '提示', {
      //   confirmButtonText: '确定',
      //   cancelButtonText: '取消',
      //   type: 'warning'
      // }).then(() => {
      //   console.log(1111)
      //   this.$axios
      //     .post('/api/markdown/save', {
      //       id: this.article.id,
      //       title: this.article.articleTitle,
      //       md: value,
      //       html: render
      //     }).then(resp => {
      //       console.log(resp)
      //       if (resp && resp.status === 200) {
      //         this.$message({
      //           type: 'info',
      //           message: '已保存成功'
      //         })
      //       }
      //     })
      // }
      // ).catch(() => {
      //   this.$message({
      //     type: 'info',
      //     message: '已取消发布'
      //   })
      // })
    },
    // 上传图片
    handleEditorImgAdd(place, $file) {
      const formdata = new FormData()
      formdata.append('file', $file)
      request({
        url: '/api/markdown/upload',
        method: 'post',
        // cmd: "POSTImgUpload", //POSTAdminInvitationAdd
        data: formdata

      }).then(res => {
        console.log(res)
        if (res.code === 20000) {
          this.$message.success('上传成功')
          // let url = res.data.url.replace(/\\/g, "/");
          // 第二步.将返回的url替换到文本原位置![...](0) -> ![...](url)  这里是必须要有的
          this.$refs.md.$img2Url(place, res.data.url)
        } else {
          this.$message.error(res.msg)
        }
      })
    },
    guid() {
      return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(
        c
      ) {
        const r = (Math.random() * 16) | 0
        const v = c === 'x' ? r : (r & 0x3) | 0x8
        return v.toString(16)
      })
    }
  }
}
</script>

<style scoped>
</style>
