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
          :router="true"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          background-color="#20222A"
          text-color="#fff"
          active-text-color="#ffd04b">
          <el-submenu index="/site">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>网站设置</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/site/index">基础配置</el-menu-item>
              <el-menu-item index="/site/emial">邮件服务</el-menu-item>
              <el-menu-item index="/site/expand">拓展属性</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="/user">
            <template slot="title">
              <i class="el-icon-menu"></i>
              <span>用户管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/user/index">基础配置</el-menu-item>
              <el-menu-item index="/user/admin">管理员</el-menu-item>
              <el-menu-item index="/user/role">用户角色</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index="/cate">
            <i class="el-icon-location"></i>
            <span>分类管理</span>
          </el-menu-item>
          <el-menu-item index="/tag">
            <i class="el-icon-location"></i>
            <span>标签管理</span>
          </el-menu-item>
          <el-submenu index="/article">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>文章管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/article/index">文章列表</el-menu-item>
              <el-menu-item index="/article/add">新增文章</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index="/backup">
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
