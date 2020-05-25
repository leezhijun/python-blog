<template>
  <header class="top-header">
    <div class="content clearfix">
      <a href="/" class="logo mr10 c000 fl"><i class="iconfont icon-kingleoric f24"></i></a>
      <ul class="top-menu">
        <li class="easing"><i class="iconfont icon-about"></i>关于</li>
        <li class="easing"><i class="iconfont icon-cc-archive"></i>归档</li>
        <li class="easing"><i class="iconfont icon-i-message"></i>留言</li>
        <li class="easing"><i class="iconfont icon-Link"></i>邻居</li>
        <li class="easing"><i class="iconfont icon-img"></i>图集</li>
      </ul>
      <div class="top-right">
        <ul class="fl">
          <li>登陆</li>
          <li>皮肤</li>
        </ul>
        <div  class="fl ml20">
          <input type="text" placeholder="查找..." /></div>
        </div>
    </div>
  </header>
</template>
<script>
export default {
  name: 'TopBar'
}
</script>
<style lang="scss" scoped>
.top-header{
  // position: sticky;
  // top: 0;
  z-index: 99;
  width: 100%;
  height: 50px;
  color: #000;
  line-height: 50px;
  background-color: rgba(190, 179, 228, 0.3);
  box-shadow: 0 -1px 4px 1px #d8d3c0;
}
.top-menu{
  float: left;
  li{
    float: left;
    padding: 0 15px;
    text-shadow: 0 1px 1px #666;
    &:hover{
      background-color: rgba(255, 255, 255, 0.1);
    }
  }
  i{
    margin-right: 2px;
  }
}
.top-right{
  float: right;
  color: #000;
  li{
    float: left;
    padding: 0 15px;
    text-shadow: 0 1px 1px #666;
  }
  input{
    font-size: 12px;
    height: 26px;
    padding: 0 10px;
    border-radius: 4px;
    background-color: rgba($color:#fff, $alpha: 0.7);
  }
}
</style>
