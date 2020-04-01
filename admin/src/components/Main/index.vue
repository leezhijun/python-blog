<template>
  <el-main>
    <transition name="fade-transform" mode="out-in">
      <keep-alive :include="cachedViews">
        <router-view :key="key" />
      </keep-alive>
    </transition>
  </el-main>
</template>
<script>
export default {
  name: 'Main',
}
</script>
<style lang="scss" scoped>

</style>
