<template>
  <div class="app-container">
    <el-button type="primary" icon="el-icon-search">搜索</el-button>
    <el-form>
      <el-form-item label="实现一（自动上传）" prop="test_file">
        <el-upload
          ref="upload"
          :limit="1"
          :file-list="fileList"
          :auto-upload="true"
          action="http://127.0.0.1:5000/api/report/upload"
          :on-success="uploadSuccess"
          :on-error="uploadErrors"
          :show-file-list="false"
        >
          <el-button size="small" type="primary">点击上传</el-button>
          <div slot="tip" class="el-upload__tip">{{tips}}</div>
        </el-upload>
      </el-form-item>
      <el-form-item label="实现二（自定义上传）" prop="test_file">
        <el-upload
          :limit="1"
          :file-list="fileList"
          action="http://127.0.0.1:5000/api/report/upload"
          :http-request="uploadeFile"
          :on-success="uploadSuccess"
        >
          <el-button size="small" type="primary">点击上传</el-button>
          <div slot="tip" class="el-upload__tip">只能上传XX/XX/XX文件，且不超过...M(通过FileField做格式限制，用secure_filename做文件名安全处理</div>
        </el-upload>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DemoUpload',
  data() {
    return {
      fileList: [],
      fileNanme: '',
      tips: '有重名文件再次上传会被覆盖掉，一般作为一个静态资源或者文件服务来说是要做生成唯一码名称，python可以使用uuid，但是对于统一文件多次反复上传就要做真正的数据文件信息存储，然后做MD5校验'
    }
  },
  methods: {
    uploadSuccess(response, file, fileList) {
      if (response.code === 40000) {
        this.$message({
          message: '格式不正确或者上传异常',
          type: 'warning'
        })
        this.fileList = []
      } else {
        this.$message({
          message: '上传成功',
          type: 'success'
        })
      }
      this.$refs.upload.clearFiles()
      this.tips = file.name
    },
    uploadErrors(err, file, fileList) {
      this.$message({
        message: '大小不符合要求或服务器异常',
        type: 'warning'
      })
    },
    uploadeFile(params) {
      console.log(params)
      const fd = new FormData()
      fd.append('file', params.file)
      fd.append('FileName', params.file.name)
      fd.append('async', true)
      const config = {
        headers: { 'Content-Type': 'multipart/form-data' }
      }
      axios
        .post(params.action, fd, config)
        .then(res => {
          console.log(res.data)
        })
        .catch(Error => {
          this.fileList = []
          this.$message({
            message: '大小不符合要求或服务器异常',
            type: 'warning'
          })
        })
    }
  }
}
</script>

<style scoped>

</style>
