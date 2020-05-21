<template>
  <ul class="breadcrumb clearfix">
    <li><a href="/"><i class="iconfont icon-home f12"></i>首页</a></li>
    <li v-if="obj"><a :href="obj.href"></a>{{obj.name}}</li>
  </ul>
</template>
<script>
export default {
  name: 'Breadcrumb',
  props: ['obj']
}
</script>
<style lang="scss" scoped>
.breadcrumb{
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #fff;
  box-shadow: 0px 1px 2px 1px #e0dfdb;
  background-color: #f7f6f1;
  li{
    float: left;
    font-size: 12px;
    margin-right: 20px;
    position: relative;
    &::after{
      content: '/';
      position: absolute;
      right: -10px;
    }
  }
  a{
    color: #857E6D;
  }
}

</style>
