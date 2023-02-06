<template>
  <div id="app">
    <router-view />
    <i class="el-icon-edit"></i>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="scss">
@import "./assets/css/icon.css";
@import '@/plugins/d3-context-menu.scss';
</style>
