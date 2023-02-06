<!--
<template>
  <div class="gContainer">
    &lt;!&ndash; <d3graph /> &ndash;&gt;
    &lt;!&ndash; <gSearch @getData="update" /> &ndash;&gt;
    <div style="margin-top: 20px;width: 1200px;">
      <el-button
          slot="append"
          type="success"
          icon="el-icon-search"
          @click="dataSwitch"
      >图数据切换</el-button>
    </div>
    <d3graph
        :data="data"
        :names="names"
        :labels="labels"
        :linkTypes="linkTypes"
        @updateNode="updateData"
    />
  </div>
</template>
<script>
// import gSearch from '@/components/gSearch.vue'
import d3graph from '@/components/d3graph.vue'
import {getAllData} from '@/api/neo4j'

export default {
  components: {
    d3graph
  },
  data() {
    return {
      // d3jsonParser()处理 json 后返回的结果
      data: {
        nodes: [],
        links: []
      },
      num:1,
      // names: ['企业', '贸易类型', '地区', '国家'],
      // labels: ['Enterprise', 'Type', 'Region', 'Country'],
      // linkTypes: ['', 'type', 'locate', 'export']
      names: ['学科', '教学内容', 'layout', '分支概念', '练习', '工具'],
      labels: ['subject', 'chapter', 'subsection', 'branch', 'practice', 'tool'],
      linkTypes: ['contain', 'tool']
    }
  },
  methods: {
    // 视图更新
    update(json) {
      console.log('update')
      console.log(json)
      this.d3jsonParser(json)
    },
    /*eslint-disable*/
    // 解析json数据，主要负责数据的去重、标准化
    d3jsonParser (json) {
      const nodes =[]
      const links = [] // 存放节点和关系
      const nodeSet = [] // 存放去重后nodes的id

      // 使用vue直接通过require获取本地json，不再需要使用d3.json获取数据
      // d3.json('./../data/records.json', function (error, data) {
      //   if (error) throw error
      //   graph = data
      //   console.log(graph[0].p)
      // })

      for (let item of json) {
        for (let segment of item.p.segments) {
          // 重新更改data格式
          if (nodeSet.indexOf(segment.start.identity) == -1) {
            nodeSet.push(segment.start.identity)
            nodes.push({
              id: segment.start.identity,
              label: segment.start.labels[0],
              properties: segment.start.properties
            })
          }
          if (nodeSet.indexOf(segment.end.identity) == -1) {
            nodeSet.push(segment.end.identity)
            nodes.push({
              id: segment.end.identity,
              label: segment.end.labels[0],
              properties: segment.end.properties
            })
          }
          links.push({
            source: segment.relationship.start,
            target: segment.relationship.end,
            type: segment.relationship.type,
            properties: segment.relationship.properties
          })
        }
      }
      console.log(nodes)
      console.log(links)
      // this.links = links
      // this.nodes = nodes
      this.data = { nodes, links }
      //  return { nodes, links }
    },
    // 从新获取数据
    updateData(){
      console.log('新增节点触发父节点的数据改变')
      this.getData('Memory Safety and Programming Language Design',this.num)
    },
    getData(name,num){
      getAllData(name,num).then(res=>{
        console.log(res)
        this.data = {}

        this.data.links = res.data.links
        this.data.nodes = res.data.nodes
        console.log(this.data)
      })
    },
    dataSwitch(){
      if(this.num == 1){
        this.num = ''
        this.getData('Memory Safety and Programming Language Design',this.num)
      }else{
        this.num = 1
        this.getData('Memory Safety and Programming Language Design',this.num)
      }
    }
  },
  created() {
    this.getData('Memory Safety and Programming Language Design',this.num)
  },
}
</script>

<style lang="scss" scoped>
.gContainer {
  position: relative;
  border: 2px rgb(44, 44, 44) solid;
  background-color: rgba(212, 212, 213, 0.76);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
</style>
-->































<template>
  <div class="gContainer">
    <!-- <d3graph /> -->
    <!-- <gSearch @getData="update" /> -->
    <!--    <div style="margin-top: 20px;width: 1200px;">
          <el-button
              slot="append"
              type="success"
              icon="el-icon-search"
              @click="dataSwitch"
          >图数据切换</el-button>
        </div>-->

    <d3graph
        :data="data"
        :names="names"
        :labels="labels"
        :linkTypes="linkTypes"
        @updateNode="updateData"
    />
  </div>
</template>
<script>
import gSearch from '@/components/gSearch.vue'
import d3graph from '@/components/d3graph.vue'
import {getAllData} from '@/api/neo4j'
export default {
  components: {
    gSearch,
    d3graph
  },
  data() {
    return {
      // d3jsonParser()处理 json 后返回的结果
      data: {
        nodes: [],
        links: []
      },
      num:'',
      // names: ['企业', '贸易类型', '地区', '国家'],
      // labels: ['Enterprise', 'Type', 'Region', 'Country'],
      // linkTypes: ['', 'type', 'locate', 'export']
      names: ['学科', '章', '节', '小节', '分支', '实验'],
      labels: ['subject', 'chapter', 'subsection', 'branch', 'subbranch', 'practice'],
      linkTypes: ['contain', 'In-class practice']
    }
  },
  methods: {
    // 视图更新
    update(json) {
      console.log('update')
      console.log(json)
      this.d3jsonParser(json)
    },
    /*eslint-disable*/
    // 解析json数据，主要负责数据的去重、标准化
    d3jsonParser (json) {
      const nodes =[]
      const links = [] // 存放节点和关系
      const nodeSet = [] // 存放去重后nodes的id

      // 使用vue直接通过require获取本地json，不再需要使用d3.json获取数据
      // d3.json('./../data/records.json', function (error, data) {
      //   if (error) throw error
      //   graph = data
      //   console.log(graph[0].p)
      // })

      for (let item of json) {
        for (let segment of item.p.segments) {
          // 重新更改data格式
          if (nodeSet.indexOf(segment.start.identity) == -1) {
            nodeSet.push(segment.start.identity)
            nodes.push({
              id: segment.start.identity,
              label: segment.start.labels[0],
              properties: segment.start.properties
            })
          }
          if (nodeSet.indexOf(segment.end.identity) == -1) {
            nodeSet.push(segment.end.identity)
            nodes.push({
              id: segment.end.identity,
              label: segment.end.labels[0],
              properties: segment.end.properties
            })
          }
          links.push({
            source: segment.relationship.start,
            target: segment.relationship.end,
            type: segment.relationship.type,
            properties: segment.relationship.properties
          })
        }
      }
      console.log('nodex',nodes)
      console.log('links',links)
      // this.links = links
      // this.nodes = nodes
      this.data = { nodes, links }
      //  return { nodes, links }
    },
    // 从新获取数据
    updateData(){
      console.log('新增节点触发父节点的数据改变')
      this.getData('安全编程语言设计',this.num)
    },
    getData(name,num){
      getAllData(name,num).then(res=>{
        console.log(res)
        this.data = {}
        this.data.links = res.data.links
        this.data.nodes = res.data.nodes
        console.log(this.data)
      })
    },
    dataSwitch(){
      if(this.num ==1){
        this.num = ''
        this.getData('安全编程语言设计',this.num)
      }else{
        this.num = 1
        this.getData('安全编程语言设计',this.num)
      }
    }
  },
  created() {
    this.getData('安全编程语言设计',this.num)
  },
}
</script>

<style lang="scss" scoped>
.gContainer {
  position: relative;
  border: 2px rgb(44, 44, 44) solid;
  background-color: rgba(212, 212, 213, 0.76);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
</style>
