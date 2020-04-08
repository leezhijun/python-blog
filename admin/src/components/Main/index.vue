<template>
  <el-main>
    <transition name="fade-transform" mode="out-in">
      <keep-alive>
        <router-view :key="key" />
      </keep-alive>
    </transition>
  </el-main>
</template>
<script>
export default {
  name: 'Main',
  computed: {
    key() {
      return this.$route.path
    }
  }
}
</script>
<style lang="scss" scoped>
.el-main{
  height: calc(100% - 80px);
  margin: 20px 20px 0 20px;
  padding: 10px;
  background-color: #fff;
}
</style>
