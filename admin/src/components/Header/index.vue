<template>
  <el-header class="header">
    <el-row type="flex" class="row-bg" justify="space-between">
      <el-col class="tl" :span="6">
        <i class="f18" @click="toggleCollapse" :class="{'el-icon-s-unfold':isCollapse,'el-icon-s-fold':!isCollapse}"></i>
        <span class="ml20">{{routerName}}</span>
      </el-col>
      <el-col :span="6"><div class="grid-content bg-purple-light"></div></el-col>
    </el-row>
  </el-header>
</template>
<script>
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
  background-color: #fff;
  line-height: 60px;
}
</style>
