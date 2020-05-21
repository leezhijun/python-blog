<template>
  <section class="section fl">
    <div class="banner mb10">
      <swiper
        ref="mySwiper"
        :options="swiperOptions"
      >
        <swiper-slide><img src="@/assets/img/banner1.jpg" /></swiper-slide>
        <swiper-slide><img src="@/assets/img/banner2.jpg" /></swiper-slide>
        <div
          class="swiper-pagination"
          slot="pagination"
        ></div>
      </swiper>
    </div>
    <ul class="post-list">
      <PostItem
        v-for="item in dataList"
        :key="item.article_id"
        :item='item'
      />
    </ul>
    <div class="pagination">
      <div class="pre fl">上一页</div>
      <div class="next fr">下一页</div>
    </div>
    <!-- <Pagination /> -->
  </section>
</template>
<script>
import { getArticleList } from '@/api/article';
export default {
  name: 'pageIndex',
  data() {
    return {
      swiperOptions: {
        autoplay: true, // 可选选项，自动滑动
        pagination: {
          el: '.swiper-pagination'
        }
        // Some Swiper option/callback...
      },
      pageIndex: 1,
      pageSize: 10,
      dataList: []
    };
  },
  computed: {
    swiper() {
      return this.$refs.mySwiper.$swiper;
    }
  },
  methods: {
    queryList() {
      const param = {
        data: {
          pageIndex: this.pageIndex,
          pageSize: this.pageSize
        }
      };
      getArticleList(param).then(
        res => {
          this.dataList = res.data.data;
          this.total = res.data.total;
        },
        err => {
          this.$message.error(err.msg);
          console.log(err);
        }
      );
    }
  },
  mounted() {
    this.queryList();
  }
};
</script>
<style lang="scss" scoped>
.banner {
  width: 100%;
  border-radius: 4px;
  overflow: hidden;
  img {
    width: 100%;
    border-radius: 4px;
  }
}
</style>
