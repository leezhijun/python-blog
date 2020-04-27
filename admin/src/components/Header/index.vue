<template>
  <el-header class="header">
    <el-row type="flex" class="row-bg" justify="space-between">
      <el-col class="tl" :span="6">
        <i class="f20 cursor" @click="toggleCollapse" :class="{'el-icon-s-unfold':isCollapse,'el-icon-s-fold':!isCollapse}"></i>
        <i class="f20 ml40 cursor el-icon-s-platform"></i>
        <i class="f20 ml40 cursor el-icon-refresh-right"></i>
        <span class="ml20">{{routerName}}</span>
      </el-col>
      <el-col class="tr" :span="6">
        <el-dropdown>
          <span class="el-dropdown-link">
            admin<i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>基本信息</el-dropdown-item>
            <el-dropdown-item>修改密码</el-dropdown-item>
            <el-dropdown-item @click="handleLoginOut">退出登陆</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-col>
    </el-row>
  </el-header>
</template>
<script>
import { loginOut } from '@/api/login'
import { clearToken } from '@/utils/auth.js'
import { mapGetters } from 'vuex'
export default {
  name: 'Header',
  data () {
    return {
    }
  },
  computed: {
    isCollapse() {
      // return this.$store.state.app.isCollapse
      return this.$store.getters.isCollapse
    },
    routerName() {
      return this.$route.name
    }
  },
  methods: {
    toggleCollapse() {
      this.$store.commit('toggleCollapse')
    },
    handleLoginOut() {
      console.log(11111111111111111111111111111111)
      loginOut().then(res => {
        console.log(res)
        clearToken()
        this.$router.push({ path: '/login' })
      }, err => {
        this.$message.error(err.msg);
        console.log(err)
      })
    }
  },
  mounted () {
    console.log(this.$store)
    console.log(this.$route)
  }
}
</script>
<style lang="scss" scoped>
.header{
  height: 60px;
  line-height: 60px;
  background-color: #fff;
}
</style>
