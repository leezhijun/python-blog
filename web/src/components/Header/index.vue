<template>
  <header class="menu-header clearfix">
    <div class="aside fl">
      <div class="logo"><img src="@/assets/img/logo.jpg" /></div>
      <ul class="count">
        <li>12 <br> 文章</li>
        <li>12 <br> 日志</li>
        <li>12 <br> 随笔</li>
      </ul>
    </div>
    <menu class="section fl">
      <ul class="nav">
        <li>代码</li>
        <li>分享</li>
        <li>日志</li>
        <li>随笔</li>
        <li>音乐</li>
        <li>设计</li>
        <li>杂谈</li>
      </ul>
    </menu>
  </header>
</template>
<script>
export default {
  name: 'Header'
}
</script>
<style lang="scss" scoped>
.count{
  position: relative;
  left: 124px;
  li{
    float: left;
    margin: 2px 0;
    padding: 0 10px;
    text-align: center;
    line-height: 20px;
    border-right: 1px solid #eee;
    &:last-of-type{
      border: none;
    }
  }
}
.logo{
  position: absolute;
  top: -50px;
  width: 84px;
  height: 84px;
  margin: 0 20px;
  padding: 4px;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0px 0px 2px 1px #d0d0d0;
  img{
    border-radius: 4px;
    width: 100%;
    height: 100%;
  }
}
.menu-header{
  position: relative;
  width: 100%;
  height: 48px;
  line-height: 48px;
  border-radius: 6px 6px 0 0;
  background-color: #f9f8f3;
  border: 1px solid #fff;
  box-shadow: 0px 1px 2px 1px #e0dfdb;
}
.nav{
  li{
    padding: 0 20px;
    float: left;
  }
}
</style>
