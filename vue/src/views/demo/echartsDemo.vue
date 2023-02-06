<template>
  <div class="app-container">
<!--    <div id="pieChartDemo"  style="width: 600px;height:400px;"></div>-->
    <div ref="pieChartDemo" style="width: 600px;height:400px;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'EchartsDemo',
  mounted() {
    this.initPieChart()
  },
  methods: {
    initPieChart() {
      // var chartDom = document.getElementById('pieChartDemo')
      var chartDom = this.$refs['pieChartDemo']
      var myChart = echarts.init(chartDom)
      var option = {
        title: {
          text: '这是一个主标题',
          subtext: '这是一个副标题',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: [
              { value: 20, name: '1' },
              { value: 2, name: '2' },
              { value: 1, name: '3' },
              { value: 3, name: '4' },
              { value: 5, name: '5' }
            ]
          }
        ]
      }
      option && myChart.setOption(option)
    }
  }
}
</script>

<style scoped>

</style>
