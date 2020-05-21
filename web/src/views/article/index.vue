<template>
  <section class="section fl">
    <article class="detail">
      <h1>{{obj.article_title}}</h1>
      <div class="pt10 f12">
        <span class="mr20"><i class="iconfont icon-time f12"></i>&nbsp;{{obj.article_publish_time}}</span>
        <!-- <span class="mr20"><i class="iconfont icon-liulan f12"></i>&nbsp;{{obj.article_browse_count}}</span> -->
        <span
          class="mr20"
          v-if="obj.cate_name"
        ><i class="iconfont icon-category f12"></i>&nbsp;{{obj.cate_name}}</span>
      </div>
      <div
        class="mt10 markdown-body"
        v-html="content"
      ></div>
      <div
        class="mt20"
        v-if="obj.tags"
      >
        <i class="iconfont icon-tags f12"></i><span
          v-for="i in obj.tags"
          :key="i.tag_id"
        >{{i.tag_name}}</span>
      </div>
    </article>
  </section>
</template>
<script>
import { articleSelectId } from '@/api/article';
import SimpleMDE from 'simplemde';
export default {
  name: 'pageAricle',
  data() {
    return {
      article_id: null,
      obj: {
        cate_id: 3,
        article_title: null,
        article_keywords: null,
        article_description: null,
        article_is_hot: 0,
        article_is_push: 0,
        article_img: null,
        article_content: null,
        article_publish_time: null,
        article_update_time: null,
        article_browse_count: 0,
        article_like_count: 0,
        article_status: 1,
        article_comment_status: 0,
        article_password: null,
        article_order: 10,
        article_type: 1,
        cate_name: null
      },
      content: null
    };
  },
  methods: {
    queryId() {
      const param = {
        data: {
          article_id: this.article_id
        }
      };
      articleSelectId(param).then(
        res => {
          console.log(res);
          this.obj = Object.assign({}, res.data, {
            article_is_hot: res.data.article_is_hot === 1,
            article_is_push: res.data.article_is_push === 1
          });
          this.content = SimpleMDE.prototype.markdown(res.data.article_content);
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
      console.log(this.$route.query.id);
      this.article_id = this.$route.query.id;
      this.queryId();
    }
  }
};
</script>
<style lang="scss" scoped>
.section {
  .detail {
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 4px;
    border: 1px solid #fff;
    box-shadow: 0px 1px 2px 1px #e0dfdb;
    background-color: #f7f6f1;
  }
  h1 {
    font-size: 22px;
    color: #7b7873;
    padding: 10px 0;
    border-bottom: 1px solid #e4e4e3;
  }
  .markdown-body {
    color: #6e6c66;
  }
  .markdown-body .highlight pre,
  .markdown-body pre {
    background-color: #eeeee6;
  }
}
</style>
