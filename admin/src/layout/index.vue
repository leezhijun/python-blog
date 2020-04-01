<template>
  <el-container class="h-100">
    <Aside class="h-100" />
    <el-container direction='vertical'>
      <Header />
      <Main />
      <!-- <Footer /> -->
    </el-container>
  </el-container>
</template>
<script>
import Header from '@/components/Header';
// import Footer from '@/components/Footer';
import Aside from '@/components/Aside';
import Main from '@/components/Main';
export default {
  name: 'Layout',
  components: {
    Header,
    // Footer,
    Aside,
    Main
  }
}
</script>
<style lang="scss" scoped>

</style>
