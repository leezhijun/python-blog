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
        <li v-for="item in dataList" :key="item.id" @mouseenter="item.show=true" @mouseleave="item.show=false">
          {{item.name}}
          <ul class="children" v-if="item.show">
            <li v-for="i in item.children" :key="i.id">{{i.name}}</li>
          </ul>
        </li>
      </ul>
    </menu>
  </header>
</template>
<script>
export default {
  name: 'Header',
  data () {
    return {
      dataList: [
        { name: '代码',id: 1, children: [{ name: '代码1',id: 11, }, { name: '代码2',id: 12, }], show: false },
        { name: '分享',id: 2, children: [{ name: '代码1',id: 21, }, { name: '代码2',id: 22, }], show: false },
        { name: '日志',id: 3, children: [{ name: '代码1',id: 31, }, { name: '代码2',id: 32, }], show: false },
        { name: '随笔',id: 4 , show: false },
        { name: '音乐',id: 5 , show: false },
        { name: '设计',id: 6 , show: false },
        { name: '杂谈',id: 7 , show: false },
      ]
    }
  }
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
    position: relative;
    padding: 0 20px;
    float: left;
    .children{
      width: 120px;
      padding: 0 10px;
      position: absolute;
      left: 0;
      z-index: 99;
      background-color: #f9f8f3;
      box-shadow: 0px 1px 2px 1px #e0dfdb;
    }
    li{
      width: 100%;
      font-size: 14px;
      line-height: 1;
      padding: 10px;
      padding-bottom: 10px;
      border-bottom: 1px dashed #d9d2c0;
      &:last-of-type{
        border: none;
      }
    }
  }
}
</style>
