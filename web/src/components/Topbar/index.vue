<template>
  <header class="top-header">
    <div class="content clearfix">
      <ul class="top-menu">
        <li class="top-logo"><img src="@/assets/img/logo.png" /></li>
        <li>关于</li>
        <li>归档</li>
        <li>留言</li>
        <li>邻居</li>
        <li>图集</li>
      </ul>
      <ul class="top-right">
        <li>登陆</li>
        <li>皮肤</li>
        <li>
          <input
            type="text"
            placeholder="查找"
          ></li>
      </ul>
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
  width: 100%;
  height: 50px;
  line-height: 50px;
  background-color: rgba(190, 179, 228, 0.3);
  box-shadow: 0 -1px 4px 1px #d8d3c0;
}
.top-menu{
  float: left;
  color: #000;
  li{
    float: left;
    padding: 0 15px;
    text-shadow: 0 1px 1px #666;
  }
  .top-logo{
    width: 200px;
    height: 50px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    img{
      display: block;
      width: 200px;
    }
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
}
</style>
