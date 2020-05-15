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
            <PostItem />
          </ul>
          <div class="pagination">
            <div class="pre fl">上一页</div>
            <div class="next fr">下一页</div>
          </div>
          <!-- <Pagination /> -->
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
.banner{
  width: 100%;
  border-radius: 4px;
  overflow: hidden;
  img{
    width: 100%;
    border-radius: 4px;
  }
}
.pagination{
  margin-top: 50px;
  .pre,.next{
    width: 80px;
    height: 28px;
    line-height: 28px;
    text-align: center;
    border-radius: 4px;
    background-color: #f7f6f1;
    border: 1px solid #fff;
    box-shadow: 0px 1px 6px 1px #d0d0d0;
  }
}
</style>
