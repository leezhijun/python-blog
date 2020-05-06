<template>
  <div class="page-index clearfix">
    <header class="top-header">
      <div class="content clearfix">
        <ul class="top-menu">
          <li>kingleoric</li>
          <li>关于</li>
          <li>归档</li>
          <li>留言</li>
          <li>邻居</li>
          <li>图集</li>
        </ul>
        <ul class="top-right">
          <li>登陆</li>
          <li>皮肤</li>
          <li><input type="text" placeholder="查找"></li>
        </ul>
      </div>
    </header>
    <section class="content blog-content clearfix">
      <header class="menu-header clearfix">
        <div class="aside fl">
          <div class="logo"><img src="@/assets/img/logo.png" /></div>
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
      <section class="mt10 clearfix">
        <aside class="aside fl">
          <aside class="aside-box">这是一个博客，纯属无聊不知道做什么，就做了这样一个博客玩，用于学习总结和知识归纳，不积跬步无以至千里，长路漫漫其修远兮，吾将上下而求索!</aside>
          <aside class="aside-box">
            <img src="@/assets/img/ad.jpg" />
          </aside>
          <aside class="aside-box">
            <h3>标签</h3>
            <div class="tags">
              <span v-for="(item,index) in tagList" :key='index'>{{item}}</span>
            </div>
          </aside>
          <aside class="aside-box">
            <h3>博客统计</h3>
            <ul>
              <li>日志总数：123</li>
              <li>文章总数：123</li>
              <li>标签总数：123</li>
              <li>运行天数：456</li>
              <li>建站日期：2020-5-5</li>
            </ul>
          </aside>
        </aside>
        <section class="section fl">
          <div class="banner">
            <swiper ref="mySwiper" :options="swiperOptions">
              <swiper-slide><img src="@/assets/img/banner1.jpg" /></swiper-slide>
              <swiper-slide><img src="@/assets/img/banner2.jpg" /></swiper-slide>
              <div class="swiper-pagination" slot="pagination"></div>
            </swiper>
          </div>
          <ul class="post-list mt10">
            <li class="post-item">
              <div class="post-content">
                <h3 class="title">Hooks & Mobx 只需额外知道两个 Hook，便能体验到如此简单的开发方式</h3>
                <div class="des">本文主要讲解了下我平时在工作开发中遇到的关于 Hooks 的一切缺点和问题，并尝试配合 Mobx 解决这些问题的经历。我觉得两者的配合可以极大的降低开发过程中有可能出现的问题以及极大的提高开发体验，而且学习成本也是非常的低。</div>
              </div>
              <div class="post-others">

              </div>
            </li>
          </ul>
        </section>
      </section>
    </section>
  </div>
</template>
<script>
export default {
  name: 'pageIndex',
  data() {
    return {
      swiperOptions: {
        autoplay: true,// 可选选项，自动滑动
        pagination: {
          el: '.swiper-pagination'
        },
        // Some Swiper option/callback...
      },
      tagList: ['html','css', '网页设计', 'javascript','vue', '思维导图', 'react','python','linux','算法']
    }
  },
  computed: {
    swiper() {
      return this.$refs.mySwiper.$swiper
    }
  },
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
.content{
  width: 1200px;
  margin: 0 auto;
}
.top-menu{
  float: left;
  li{
    float: left;
    padding: 0 15px;
    text-shadow: 0 1px 1px #666;
  }
}
.top-right{
  float: right;
  li{
    float: left;
    padding: 0 15px;
    text-shadow: 0 1px 1px #666;
  }
}
.blog-content{
  // position: relative;
  // top: 180px;
  // height: 100%;
  margin-top: 180px;
  padding-bottom: 40px;
  border-radius: 6px;
  background-color: #ebe8e1;
  border: 1px solid #fff;
  box-shadow: 0px 1px 4px 1px #8c8a84;
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
.aside{
  width: 300px;
}
.section{
  width: calc( 100% - 310px);
  .post-item{
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 4px;
    border: 1px solid #fff;
    box-shadow: 0px 1px 2px 1px #e0dfdb;
    background-color: #f7f6f1;
  }
}
.nav{
  li{
    padding: 0 20px;
    float: left;
  }
}
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
      box-shadow: 0 0 2px 1px #b3b3b3 inset;
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
      padding: 6px 10px;
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
}
.banner{
  width: 100%;
  border-radius: 4px;
  overflow: hidden;
  img{
    width: 100%;
  }
}

</style>
