<template>
  <section class="section fl">
    <ul class="post-list mt10">
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
  </section>
</template>
<script>
import { getArticleList } from '@/api/article';
export default {
  name: 'pageTag',
  data () {
    return {
      tag_id: null,
      pageIndex: 1,
      pageSize: 10,
      dataList: [],
    }
  },
    methods: {
    queryList() {
      const param = {
        data: {
          tag_id: this.tag_id,
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
    if (this.$route.query.id) {
      this.tag_id = this.$route.query.id;
      this.queryList();
    }
  }
};
</script>
