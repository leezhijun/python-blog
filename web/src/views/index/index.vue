<template>
  <div class="page-index clearfix">
    <Topbar />
    <section class="content blog-content clearfix">
      <Header />
      <section class="mt10 clearfix">
        <Aside />
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
              <div class="post-content clearfix">
                <h3 class="title">Hooks & Mobx 只需额外知道两个 Hook，便能体验到如此简单的开发方式</h3>
                <div class="des">本文主要讲解了下我平时在工作开发中遇到的关于 Hooks 的一切缺点和问题，并尝试配合 Mobx 解决这些问题的经历。我觉得两者的配合可以极大的降低开发过程中有可能出现的问题以及极大的提高开发体验，而且学习成本也是非常的低。</div>
              </div>
              <div class="post-others">
                <span class="tiem">2020-10-01 12:12:12</span>
                <span class="author">kingleric</span>
                <span class="tag"></span>
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
.section{
  .post-item{
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 4px;
    border: 1px solid #fff;
    box-shadow: 0px 1px 2px 1px #e0dfdb;
    background-color: #f7f6f1;
  }
  .post-content{
    .img{
      float: left;
      // position: relative;
      // top: -80px;
      transform:translateY(-80px);
      width: 200px;
      height: 180px;
      margin-right: 15px;
      padding: 5px;
      border-radius: 2px;
      background-color: #fff;
      img{
        width: 100%;
        border-radius: 2px;
      }
    }
  }
  .title{
    padding: 10px 0;
    font-size: 18px;
    color: #817E74;
    border-bottom: 1px solid #EEEEE6;
  }
  .des{
    margin-top: 15px;
    margin-bottom: 15px;
    font-size: 14px;
    color: #B4B0A4;
    line-height: 1.4;
  }
  .post-others{
    border-top: 1px solid #EEEEE6;
    padding-top: 10px;
    font-size: 12px;
    color: #9F9D92;
  }
}
.banner{
  width: 100%;
  border-radius: 4px;
  overflow: hidden;
  img{
    width: 100%;
    border-radius: 4px;
  }
}

</style>
