<template>
  <div id="app">
    <el-container direction='vertical'>
      <Header />
      <el-container>
        <Aside />
        <Main />
      </el-container>
      <Footer />
    </el-container>
  </div>
</template>
<script>
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import Aside from '@/components/Aside';
import Main from '@/components/Main';

export default {
  name: 'App',
  components: {
    Header,
    Footer,
    Aside,
    Main
  }
};
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
