<template>
  <aside class="aside fl">
    <aside class="aside-box">
      <div class="f12">这是一个博客，很早以前就想自己写个博客的，用于学习总结和知识归纳，不积跬步无以至千里，长路漫漫其修远兮，吾将上下而求索!</div>
      <ul class="icon-list">
        <li><i class="iconfont icon-weibo"></i></li>
        <li><i class="iconfont icon-qq"></i></li>
        <li><i class="iconfont icon-weixin"></i></li>
        <li><i class="iconfont icon-github"></i></li>
        <li><i class="iconfont icon-bilibili-line"></i></li>
      </ul>
    </aside>
    <aside class="aside-box">
      <img src="@/assets/img/ad.jpg" />
    </aside>
    <aside class="aside-box">
      <h3>标签</h3>
      <div class="tags">
        <span
          v-for="(item,index) in tagList"
          :key='index'
        >{{item}}</span>
      </div>
    </aside>
    <aside class="aside-box f12">
      <h3>博客统计</h3>
      <ul>
        <li>日志总数：--</li>
        <li>文章总数：--</li>
        <li>标签总数：--</li>
        <li>运行天数：{{days}}</li>
        <li>建站日期：2020-5-25</li>
      </ul>
    </aside>
  </aside>
</template>
<script>
export default {
  name: 'Aside',
  data () {
    return {
      days: '--',
      tagList: ['html','css', '网页设计', 'javascript','vue', '思维导图', 'react','python','linux','算法']
    }
  },
  methods: {
    getDays() {
      const timestamp = (new Date("2020/05/25 00:00:00")).getTime();
      const timeNow = new Date().getTime()
      if (timestamp<timeNow) {
        const cha = (timeNow - timestamp)/(1*24*60*60*1000)
        this.days = Math.ceil(cha)
      }
    }
  },
  mounted () {
    this.getDays()
  }
}
</script>
<style lang="scss" scoped>
.aside-box{
  margin: 0 10px 10px 10px;
  padding: 10px;
  line-height: 1.4;
  border-radius: 4px;
  background-color: #f7f6f2;
  border: 1px solid #fff;
  box-shadow: 0px 1px 6px 1px #d0d0d0;
  img{
    width: 100%;
    height: auto;
    vertical-align: bottom;
  }
  h3{
    position: relative;
    font-size: 16px;
    text-align: center;
    padding-bottom: 10px;
    border-bottom: 1px solid #e4e4e3;
    &::before,&::after{
      position: absolute;

      top:8px;
      content: '';
      width: 8px;
      height: 8px;
      border-radius: 8px;
      background-color: #c5c5c5;
      border: 1px solid #e2e2e2;
      // box-shadow: 0 0 2px 1px #b3b3b3 inset;
      box-shadow: 0 0 1px #f7f6f1 inset, 1px 1px 1px #817e74 inset;
    }
    &::after{
      right: 4px;
    }
    &::before{
      left: 4px;
    }
  }
  .tags{
    span{
      display: inline-block;
      font-size: 12px;
      padding: 0 4px;
      margin-right: 10px;
      margin-top: 10px;
      border-radius: 4px;
      border: 1px solid #d9d2c0;
    }
  }
  li{
    padding: 10px 0;
    border-bottom: 1px solid #eee;
  }
  .icon-list{
    margin-top: 10px;
    padding-top: 5px;
    border-top: 1px solid #eeedea;
    display: flex;
    justify-content: space-around;
    li{
      padding: 0;
      border: none;
    }
    i{
      text-shadow: 1px 1px 1px #d9d2c0, -1px -1px 1px #fff;
    }
  }
}
</style>
