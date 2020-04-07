<template>
  <div class="aside" :style="{width: isCollapse ? '64px' : '220px'}">
    <div class="aside-admin">
      <h2 class="f18 tc" v-if="!isCollapse">blogAdmin</h2>
      <h2 class="tc" v-else><i class="el-icon-s-promotion f24"></i></h2>
    </div>
    <div style="height:calc(100% - 60px);overflow-x: hidden;">
      <el-scrollbar wrap-class="scrollbar-wrapper">
        <el-menu
          :collapse="isCollapse"
          :collapse-transition="false"
          :unique-opened="true"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          background-color="#20222A"
          text-color="#fff"
          active-text-color="#ffd04b">
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>网址设置</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="1-1">基础信息</el-menu-item>
              <el-menu-item index="1-2">新增属性</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index="2">
            <i class="el-icon-menu"></i>
            <span slot="title">用户管理</span>
          </el-menu-item>
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>分类管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="1-1">分类列表</el-menu-item>
              <el-menu-item index="1-2">新增分类</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="4">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>标签管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="1-1">标签列表</el-menu-item>
              <el-menu-item index="1-2">新增标签</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="5">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>文章管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="1-1">文章列表</el-menu-item>
              <el-menu-item index="1-2">新增文章</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index="6">
            <i class="el-icon-menu"></i>
            <span slot="title">备份管理</span>
          </el-menu-item>
        </el-menu>
      </el-scrollbar>
    </div>

  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Aside',
  computed: {
    ...mapGetters([
      'isCollapse',
    ]),
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>
<style lang="scss" scoped>
.aside{
  height: 100%;
  color: #FFF;
  background-color: #20222A;
  transition: all .3s;
}
.aside-admin h2{
  height: 60px;
  line-height: 60px;
  color: #c0c4cc;
}
.el-menu{
  border: none;
}
</style>
